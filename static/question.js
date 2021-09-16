//페이지 로드되면 바로 실행
$(document).ready(function () {
    getQuiz(1);
    dragon();
    showLike();
})

let idx = 1
let ans = '';

// 퀴즈 내용을 불러오는 명령 getQuiz() 'GET'
function getQuiz(idx) {
    console.log("%d번째 문제입니다.", idx)
    $.ajax({
        url: `/quiz?idx=${idx}`,
        method: 'GET',
        success: function (response) {
            $('.Question').empty();
            let data = response["quiz"][0];

            console.log("idx :" + data["idx"]);

            $('.Question').append(`<h2 class ="Q-num" > Q${data["idx"]}.</h2> <h2 class ="Q-2"  >${data["quiz"]}</h2>`)

            $('#type_A').html(makeHtml(`${data["ans_01"]}`))
            $('#type_B').html(makeHtml(`${data["ans_02"]}`))
            $('#type_C').html(makeHtml(`${data["ans_03"]}`))
            $('#type_D').html(makeHtml(`${data["ans_04"]}`))

            $('#img_A').css('background-image', `url(${(data["ans_img01"])})`)
            $('#img_B').css('background-image', `url(${(data["ans_img02"])})`)
            $('#img_C').css('background-image', `url(${(data["ans_img03"])})`)
            $('#img_D').css('background-image', `url(${(data["ans_img04"])})`)
        }
    })
}

function makeHtml(data) {
    let tempHtml = `
              <p> ${data} </p>
            `
    return tempHtml;
}

// 선택했던 내용을 기억하는 명령
function ans_click(x) {
    console.log("%s 선택.", x)

    let cel = idx / 6 * 100
    console.log(cel)

    document.getElementById('progress-bar').style.width = `${cel}%`

    ans += x;
    idx += 1;
    if (idx > 6) {
        alert("최종 응답 유형은 " + ans)
        location.href = `/answer?type=${ans}`;
        return;
    }

    // let pgs = document.getElementsByClassName("progress-bar");
    // pgs.style.width = "50%"
    getQuiz(idx, x)
}

//좋아요 하트변환 & 좋아요 DB반영 부분

var cnt = 1;

function likered() {
    var heart = document.getElementById("heart");
    $('p').remove('.liketext')
    if (cnt%2==1) {
        // console.log(cnt);
        heart.src = "data:image/svg+xml;base64,PD94bWwgdmVyc2lvbj0iMS4wIiBlbmNvZGluZz0iaXNvLTg4NTktMSI/Pg0KPCEtLSBHZW5lcmF0b3I6IEFkb2JlIElsbHVzdHJhdG9yIDE4LjAuMCwgU1ZHIEV4cG9ydCBQbHVnLUluIC4gU1ZHIFZlcnNpb246IDYuMDAgQnVpbGQgMCkgIC0tPg0KPCFET0NUWVBFIHN2ZyBQVUJMSUMgIi0vL1czQy8vRFREIFNWRyAxLjEvL0VOIiAiaHR0cDovL3d3dy53My5vcmcvR3JhcGhpY3MvU1ZHLzEuMS9EVEQvc3ZnMTEuZHRkIj4NCjxzdmcgdmVyc2lvbj0iMS4xIiBpZD0iQ2FwYV8xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHhtbG5zOnhsaW5rPSJodHRwOi8vd3d3LnczLm9yZy8xOTk5L3hsaW5rIiB4PSIwcHgiIHk9IjBweCINCgkgdmlld0JveD0iMCAwIDU3Ljk0NyA1Ny45NDciIHN0eWxlPSJlbmFibGUtYmFja2dyb3VuZDpuZXcgMCAwIDU3Ljk0NyA1Ny45NDc7IiB4bWw6c3BhY2U9InByZXNlcnZlIj4NCjxnPg0KCTxwYXRoIHN0eWxlPSJmaWxsOiNFNjRDM0M7IiBkPSJNMjguOTQ3LDU2LjQ4NmMxNS42ODUtMTEuMjc3LDIzLjUzMi0yMS41OTIsMjcuMjIyLTI5LjQ2YzQuMzExLTkuMTkzLDAuNTYxLTIwLjU4OS04Ljg0NS0yNC40MTMNCgkJQzM2LjI2OC0xLjg4LDI4Ljk0Nyw4LjQ4NiwyOC45NDcsOC40ODZTMjEuNjc4LTEuOTA3LDEwLjYyMywyLjU4OEMxLjIxNyw2LjQxMi0yLjUzMywxNy44MDgsMS43NzgsMjcuMDAxDQoJCUM1LjQ2OCwzNC44NjgsMTMuMjYyLDQ1LjIxLDI4Ljk0Nyw1Ni40ODZ6Ii8+DQo8L2c+DQo8Zz4NCjwvZz4NCjxnPg0KPC9nPg0KPGc+DQo8L2c+DQo8Zz4NCjwvZz4NCjxnPg0KPC9nPg0KPGc+DQo8L2c+DQo8Zz4NCjwvZz4NCjxnPg0KPC9nPg0KPGc+DQo8L2c+DQo8Zz4NCjwvZz4NCjxnPg0KPC9nPg0KPGc+DQo8L2c+DQo8Zz4NCjwvZz4NCjxnPg0KPC9nPg0KPGc+DQo8L2c+DQo8L3N2Zz4NCg==";
        cnt ++;
        return likePlus();

    } else {
        // console.log(cnt);
        heart.src = "data:image/svg+xml;base64,PHN2ZyB2aWV3Qm94PSIwIC0yOCA1MTIuMDAxIDUxMiIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj48cGF0aCBkPSJtMjU2IDQ1NS41MTU2MjVjLTcuMjg5MDYyIDAtMTQuMzE2NDA2LTIuNjQwNjI1LTE5Ljc5Mjk2OS03LjQzNzUtMjAuNjgzNTkzLTE4LjA4NTkzNy00MC42MjUtMzUuMDgyMDMxLTU4LjIxODc1LTUwLjA3NDIxOWwtLjA4OTg0My0uMDc4MTI1Yy01MS41ODIwMzItNDMuOTU3MDMxLTk2LjEyNS04MS45MTc5NjktMTI3LjExNzE4OC0xMTkuMzEyNS0zNC42NDQ1MzEtNDEuODA0Njg3LTUwLjc4MTI1LTgxLjQ0MTQwNi01MC43ODEyNS0xMjQuNzQyMTg3IDAtNDIuMDcwMzEzIDE0LjQyNTc4MS04MC44ODI4MTMgNDAuNjE3MTg4LTEwOS4yOTI5NjkgMjYuNTAzOTA2LTI4Ljc0NjA5NCA2Mi44NzEwOTMtNDQuNTc4MTI1IDEwMi40MTQwNjItNDQuNTc4MTI1IDI5LjU1NDY4OCAwIDU2LjYyMTA5NCA5LjM0Mzc1IDgwLjQ0NTMxMiAyNy43Njk1MzEgMTIuMDIzNDM4IDkuMzAwNzgxIDIyLjkyMTg3NiAyMC42ODM1OTQgMzIuNTIzNDM4IDMzLjk2MDkzOCA5LjYwNTQ2OS0xMy4yNzczNDQgMjAuNS0yNC42NjAxNTcgMzIuNTI3MzQ0LTMzLjk2MDkzOCAyMy44MjQyMTgtMTguNDI1NzgxIDUwLjg5MDYyNS0yNy43Njk1MzEgODAuNDQ1MzEyLTI3Ljc2OTUzMSAzOS41MzkwNjMgMCA3NS45MTAxNTYgMTUuODMyMDMxIDEwMi40MTQwNjMgNDQuNTc4MTI1IDI2LjE5MTQwNiAyOC40MTAxNTYgNDAuNjEzMjgxIDY3LjIyMjY1NiA0MC42MTMyODEgMTA5LjI5Mjk2OSAwIDQzLjMwMDc4MS0xNi4xMzI4MTIgODIuOTM3NS01MC43NzczNDQgMTI0LjczODI4MS0zMC45OTIxODcgMzcuMzk4NDM3LTc1LjUzMTI1IDc1LjM1NTQ2OS0xMjcuMTA1NDY4IDExOS4zMDg1OTQtMTcuNjI1IDE1LjAxNTYyNS0zNy41OTc2NTcgMzIuMDM5MDYyLTU4LjMyODEyNiA1MC4xNjc5NjktNS40NzI2NTYgNC43ODkwNjItMTIuNTAzOTA2IDcuNDI5Njg3LTE5Ljc4OTA2MiA3LjQyOTY4N3ptLTExMi45Njg3NS00MjUuNTIzNDM3Yy0zMS4wNjY0MDYgMC01OS42MDU0NjkgMTIuMzk4NDM3LTgwLjM2NzE4OCAzNC45MTQwNjItMjEuMDcwMzEyIDIyLjg1NTQ2OS0zMi42NzU3ODEgNTQuNDQ5MjE5LTMyLjY3NTc4MSA4OC45NjQ4NDQgMCAzNi40MTc5NjggMTMuNTM1MTU3IDY4Ljk4ODI4MSA0My44ODI4MTMgMTA1LjYwNTQ2OCAyOS4zMzIwMzEgMzUuMzk0NTMyIDcyLjk2MDkzNyA3Mi41NzQyMTkgMTIzLjQ3NjU2MiAxMTUuNjI1bC4wOTM3NS4wNzgxMjZjMTcuNjYwMTU2IDE1LjA1MDc4MSAzNy42Nzk2ODggMzIuMTEzMjgxIDU4LjUxNTYyNSA1MC4zMzIwMzEgMjAuOTYwOTM4LTE4LjI1MzkwNyA0MS4wMTE3MTktMzUuMzQzNzUgNTguNzA3MDMxLTUwLjQxNzk2OSA1MC41MTE3MTktNDMuMDUwNzgxIDk0LjEzNjcxOS04MC4yMjI2NTYgMTIzLjQ2ODc1LTExNS42MTcxODggMzAuMzQzNzUtMzYuNjE3MTg3IDQzLjg3ODkwNy02OS4xODc1IDQzLjg3ODkwNy0xMDUuNjA1NDY4IDAtMzQuNTE1NjI1LTExLjYwNTQ2OS02Ni4xMDkzNzUtMzIuNjc1NzgxLTg4Ljk2NDg0NC0yMC43NTc4MTMtMjIuNTE1NjI1LTQ5LjMwMDc4Mi0zNC45MTQwNjItODAuMzYzMjgyLTM0LjkxNDA2Mi0yMi43NTc4MTIgMC00My42NTIzNDQgNy4yMzQzNzQtNjIuMTAxNTYyIDIxLjUtMTYuNDQxNDA2IDEyLjcxODc1LTI3Ljg5NDUzMiAyOC43OTY4NzQtMzQuNjA5Mzc1IDQwLjA0Njg3NC0zLjQ1MzEyNSA1Ljc4NTE1Ny05LjUzMTI1IDkuMjM4MjgyLTE2LjI2MTcxOSA5LjIzODI4MnMtMTIuODA4NTk0LTMuNDUzMTI1LTE2LjI2MTcxOS05LjIzODI4MmMtNi43MTA5MzctMTEuMjUtMTguMTY0MDYyLTI3LjMyODEyNC0zNC42MDkzNzUtNDAuMDQ2ODc0LTE4LjQ0OTIxOC0xNC4yNjU2MjYtMzkuMzQzNzUtMjEuNS02Mi4wOTc2NTYtMjEuNXptMCAwIi8+PC9zdmc+";
        cnt ++;
        return likeMinus();
    };
}

// 마스코트 불뿜기!
function dragon() {
$('#paperplane').click(function () {
    if ($('.breathe').hasClass('breathe')) {
        $('.breathe').css('visibility', 'visible');
    }
    setTimeout(function () {
        $('.breathe').css('visibility', 'hidden');
    }, 1000);
});
}

// 좋아요 값 불러오기
function showLike() {
    $.ajax({
        type: 'GET',
        url: '/like?',
        data: {},
        success: function (response) {
            $('#likenum').empty();
            let like = response['likedb']
            let count = like[0]['count']
            let temp_thml = `<p class="liketext">좋아요 ${count}개</p>`

            $('#likenum').append(temp_thml)
        }
    });
}

// 좋아요 추가&제거 동작
function likePlus() {
    $.ajax({
        type: 'POST',
        url: '/like/+',
        data: {name_give: 'like'},
        success: function (response) {
            console.log(response)
            return showLike()
        }
    });
}

function likeMinus() {
    $.ajax({
        type: 'POST',
        url: '/like/-',
        data: {name_give: 'like'},
        success: function (response) {
            console.log(response)
            return showLike()
        }
    });
}

// 다크모드 동작
document.getElementById("toggleDark").addEventListener("click", () => {
    const html = document.documentElement;

    if (html.classList.contains("dark")) {
        html.classList.remove("dark");
        localStorage.setItem("darkTheme", "false");
    } else {
        html.classList.add("dark");
        localStorage.setItem("darkTheme", "true");
    }
});

const storedTheme = localStorage.getItem("darkTheme");

if (storedTheme !== null) {
    if (storedTheme === "true") {
        document.documentElement.classList.add("dark");
    }
} else if (window.matchMedia("(prefers-color-scheme: dark)").matches) {
    document.documentElement.classList.add("dark");
}