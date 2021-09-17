$(document).ready(function () {
    let type = getType()
    let ansType = manyKeyword(type);
    getAns(ansType);
    // $('.content-img').attr('width', '100'); 이미지 width 수정 test 작동 x
    dragon()
    showLike()
});

function getType() {
    let type = location.search.split('=')[1]
    return type;
}

function manyKeyword(type) {
    const input = type;

    const charMap = {};

    for (let char of input.toLowerCase()) {
        charMap[char] = charMap[char] ? charMap[char] + 1 : 1;
    }

    // charMap의 최대값을 max 변수에 넣어준다 Object.values는 배열로 반환해준다는 의미이다.
    let max = Math.max.apply(null, Object.values(charMap));
    let maxChar = '';
    let counter = 0;
    for (let char in charMap) {
        if (charMap[char] === max) {
            maxChar = char;
            counter++;
        }
        // 중복인 경우
        if (counter > 1) {
            return "F";
        }
    }
    return maxChar.toUpperCase();
}

function getAns(type) {
    $.ajax({
        url: `/ans?type=${type}`,
        method: 'GET',
        success: function (response) {

            $('.box').empty();

            let data = response["ans"][0];

            $('#btn-mainpic').attr('src', `${data['cover']}`)
            $('.box').append(`<h2 class ="ans">${data['type']}.</h2> <h2 class="recommend"> 당신에게 추천하는 활동은?<br> <span style="font-size: 25px; font-family: 'Jua', sans-serif;">${data['suggest']}</span></h2>`)


            if (type == 'A') // type A 산책
            {
                $('.map').css('visibility', 'visible');

            } else if (type == 'B') // type B 홈트
            {
                $('#map').hide()
                $('#top1').html(addHtml1(data['title1'], data['info1'], data['director1'], data['img_link1'], data['link1']))
                $('#top2').html(addHtml2(data['title2'], data['info2'], data['director2'], data['img_link2'], data['link2']))
                $('#top3').html(addHtml3(data['title3'], data['info3'], data['director3'], data['img_link3'], data['link3']))

                function addHtml1(title1, info1, director1, img_link1, link1) {
                    let tempHtml = `
                                <div class="num"><span style="font-size: 35px; font-weight: normal; color: white">1</span>위</div>
                                <div class="content">
                                    <span style="font-size: 17.5px;">${title1}</span>
                                    <br>  <br><br>${info1} <br>${director1}
                                </div>
                                <img class="content-img"
                                     src="${img_link1}"
                                     onclick="location.href='${link1}'">
                            `
                    return tempHtml;
                }

                function addHtml2(title2, info2, director2, img_link2, link2) {
                    let tempHtml = `
                                <div class="num"> <span style="font-size: 35px; font-weight: normal; color: white">2</span>위</div>
                                <div class="content">
                                    <span style="font-size: 17.5px;">${title2}</span>
                                    <br>  <br><br>${info2} <br>${director2}
                                </div>
                                <img class="content-img"
                                     src="${img_link2}"
                                     onclick="location.href='${link2}'">
                            `
                    return tempHtml;
                }

                function addHtml3(title3, info3, director3, img_link3, link3) {
                    let tempHtml = `
                                <div class="num"><span style="font-size: 35px; font-weight: normal; color: white">3</span>위</span></div>
                                <div class="content">
                                    <span style="font-size: 17.5px;">${title3}</span>
                                    <br>  <br><br>${info3} <br>${director3}
                                </div>
                                <img class="content-img"
                                     src="${img_link3}"
                                     onclick="location.href='${link3}'">
                            `
                    return tempHtml;
                }
            } else if (type == 'C') // type C 요리
            {
                $('#map').hide()
                $('#top1').html(addHtml1(data['title1'], data['info1'], data['director1'], data['img_link1'], data['link1']))
                $('#top2').html(addHtml2(data['title2'], data['info2'], data['director2'], data['img_link2'], data['link2']))
                $('#top3').html(addHtml3(data['title3'], data['info3'], data['director3'], data['img_link3'], data['link3']))

                function addHtml1(title1, info1, director1, img_link1, link1) {
                    let tempHtml = `
                                <div class="num"><span style="font-size: 35px; font-weight: normal; color: white">1</span>위</div>
                                <div class="content">
                                    <span style="font-size: 18px;">${title1}</span>
                                    <br>  <br><br>${info1} <br>${director1}
                                </div>
                                <img class="content-img"
                                     src="${img_link1}"
                                     onclick="location.href='${link1}'">
                            `
                    return tempHtml;
                }

                function addHtml2(title2, info2, director2, img_link2, link2) {
                    let tempHtml = `
                                <div class="num"><span style="font-size: 35px; font-weight: normal; color: white">2</span>위</div>
                                <div class="content">
                                    <span style="font-size: 18px;">${title2}</span>
                                    <br>  <br><br>${info2} <br>${director2}
                                </div>
                                <img class="content-img"
                                     src="${img_link2}"
                                     onclick="location.href='${link2}'">
                            `
                    return tempHtml;
                }

                function addHtml3(title3, info3, director3, img_link3, link3) {
                    let tempHtml = `
                                <div class="num"><span style="font-size: 35px; font-weight: normal; color: white">3</span>위</div>
                                <div class="content">
                                    <span style="font-size: 18px;">${title3}</span>
                                    <br>  <br><br>${info3} <br>${director3}
                                </div>
                                <img class="content-img"
                                     src="${img_link3}"
                                     onclick="location.href='${link3}'">
                            `
                    return tempHtml;
                }
            } else if (type == 'D') // type D 독서
            {
                $('#map').hide()
                $('#top1').html(addHtml1(data['title1'], data['genre1'], data['info1'], data['director1'], data['img_link1'], data['link1']))
                $('#top2').html(addHtml2(data['title2'], data['genre2'], data['info2'], data['director2'], data['img_link2'], data['link2']))
                $('#top3').html(addHtml3(data['title3'], data['genre3'], data['info3'], data['director3'], data['img_link3'], data['link3']))

                function addHtml1(title1, genre1, info1, director1, img_link1, link1) {
                    let tempHtml = `
                                <div class="num"><span style="font-size: 35px; font-weight: normal; color: white">1</span>위</div>
                                <div class="content">
                                    <span style="font-size: 18px;">${title1}</span>
                                    <br><span class="genre">${genre1}</span><br><br> 출판사 : ${info1} <br> 저자 : ${director1}
                                </div>
                                <img class="content-img"
                                     src="${img_link1}"
                                     onclick="location.href='${link1}'">
                            `
                    return tempHtml;
                }

                function addHtml2(title2, genre2, info2, director2, img_link2, link2) {
                    let tempHtml = `
                                <div class="num"><span style="font-size: 35px; font-weight: normal; color: white">2</span>위</div>
                                <div class="content">
                                    <span style="font-size: 18px;">${title2}</span>
                                    <br><span class="genre">${genre2}</span><br><br> 출판사 : ${info2} <br> 저자 : ${director2}
                                </div>
                                <img class="content-img"
                                     src="${img_link2}"
                                     onclick="location.href='${link2}'">
                            `
                    return tempHtml;
                }

                function addHtml3(title3, genre3, info3, director3, img_link3, link3) {
                    let tempHtml = `
                                <div class="num"><span style="font-size: 35px; font-weight: normal; color: white">3</span>위</div>
                                <div class="content">
                                    <span style="font-size: 18px;">${title3}</span>
                                    <br><span class="genre">${genre3}</span><br><br> 출판사 : ${info3} <br> 저자 : ${director3}
                                </div>
                                <img class="content-img"
                                     src="${img_link3}"
                                     onclick="location.href='${link3}'">
                            `
                    return tempHtml;
                }
            } else // type F 2,3위 시간 정보가 애매함
            {
                $('#map').hide()
                $('#top1').html(addHtml1(data['title1'], data['genre1'], data['info1'], data['director1'], data['img_link1'], data['link1']))
                $('#top2').html(addHtml2(data['title2'], data['genre2'], data['info2'], data['director2'], data['img_link2'], data['link2']))
                $('#top3').html(addHtml3(data['title3'], data['genre3'], data['info3'], data['director3'], data['img_link3'], data['link3']))

                function addHtml1(title1, genre1, info1, director1, img_link1, link1) {
                    let tempHtml = `
                                <div class="num"><span style="font-size: 35px; font-weight: normal; color: white">1</span>위</div>
                                <div class="content">
                                    <span style="font-size: 25px;">${title1}</span>
                                    <br> <span class="genre">${genre1}</span> <br><br>${info1} <br>${director1}
                                </div>
                                <img class="content-img"
                                     src="${img_link1}"
                                     onclick="location.href='${link1}'">
                            `
                    return tempHtml;
                }

                function addHtml2(title2, genre2, info2, director2, img_link2, link2) {
                    let tempHtml = `
                                <div class="num"><span style="font-size: 35px; font-weight: normal; color: white">2</span>위</div>
                                <div class="content">
                                    <span style="font-size: 25px;">${title2}</span>
                                    <br> <span class="genre">${genre2}</span> <br><br> <br>${director2}
                                </div>
                                <img class="content-img"
                                     src="${img_link2}"
                                     onclick="location.href='${link2}'">
                            `
                    return tempHtml;
                }

                function addHtml3(title3, genre3, info3, director3, img_link3, link3) {
                    let tempHtml = `
                                <div class="num"><span style="font-size: 35px; font-weight: normal; color: white">3</span>위</div>
                                <div class="content">
                                    <span style="font-size: 25px;">${title3}</span>
                                    <br> <span class="genre">${genre3}</span> <br><br><br>${director3}
                                </div>
                                <img class="content-img"
                                     src="${img_link3}"
                                     onclick="location.href='${link3}'">
                            `
                    return tempHtml;
                }
            }

        }
    })
}

function openclose() {
    $('#btn-mainpic').hide()
}

var cnt = 1;

function likered() {
    var heart = document.getElementById("heart");
    $('p').remove('.liketext')
    if (cnt % 2 == 1) {
        // console.log(cnt);
        heart.src = "data:image/svg+xml;base64,PD94bWwgdmVyc2lvbj0iMS4wIiBlbmNvZGluZz0iaXNvLTg4NTktMSI/Pg0KPCEtLSBHZW5lcmF0b3I6IEFkb2JlIElsbHVzdHJhdG9yIDE4LjAuMCwgU1ZHIEV4cG9ydCBQbHVnLUluIC4gU1ZHIFZlcnNpb246IDYuMDAgQnVpbGQgMCkgIC0tPg0KPCFET0NUWVBFIHN2ZyBQVUJMSUMgIi0vL1czQy8vRFREIFNWRyAxLjEvL0VOIiAiaHR0cDovL3d3dy53My5vcmcvR3JhcGhpY3MvU1ZHLzEuMS9EVEQvc3ZnMTEuZHRkIj4NCjxzdmcgdmVyc2lvbj0iMS4xIiBpZD0iQ2FwYV8xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHhtbG5zOnhsaW5rPSJodHRwOi8vd3d3LnczLm9yZy8xOTk5L3hsaW5rIiB4PSIwcHgiIHk9IjBweCINCgkgdmlld0JveD0iMCAwIDU3Ljk0NyA1Ny45NDciIHN0eWxlPSJlbmFibGUtYmFja2dyb3VuZDpuZXcgMCAwIDU3Ljk0NyA1Ny45NDc7IiB4bWw6c3BhY2U9InByZXNlcnZlIj4NCjxnPg0KCTxwYXRoIHN0eWxlPSJmaWxsOiNFNjRDM0M7IiBkPSJNMjguOTQ3LDU2LjQ4NmMxNS42ODUtMTEuMjc3LDIzLjUzMi0yMS41OTIsMjcuMjIyLTI5LjQ2YzQuMzExLTkuMTkzLDAuNTYxLTIwLjU4OS04Ljg0NS0yNC40MTMNCgkJQzM2LjI2OC0xLjg4LDI4Ljk0Nyw4LjQ4NiwyOC45NDcsOC40ODZTMjEuNjc4LTEuOTA3LDEwLjYyMywyLjU4OEMxLjIxNyw2LjQxMi0yLjUzMywxNy44MDgsMS43NzgsMjcuMDAxDQoJCUM1LjQ2OCwzNC44NjgsMTMuMjYyLDQ1LjIxLDI4Ljk0Nyw1Ni40ODZ6Ii8+DQo8L2c+DQo8Zz4NCjwvZz4NCjxnPg0KPC9nPg0KPGc+DQo8L2c+DQo8Zz4NCjwvZz4NCjxnPg0KPC9nPg0KPGc+DQo8L2c+DQo8Zz4NCjwvZz4NCjxnPg0KPC9nPg0KPGc+DQo8L2c+DQo8Zz4NCjwvZz4NCjxnPg0KPC9nPg0KPGc+DQo8L2c+DQo8Zz4NCjwvZz4NCjxnPg0KPC9nPg0KPGc+DQo8L2c+DQo8L3N2Zz4NCg==";
        cnt++;
        return likePlus();

    } else {
        // console.log(cnt);
        heart.src = "data:image/svg+xml;base64,PHN2ZyB2aWV3Qm94PSIwIC0yOCA1MTIuMDAxIDUxMiIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj48cGF0aCBkPSJtMjU2IDQ1NS41MTU2MjVjLTcuMjg5MDYyIDAtMTQuMzE2NDA2LTIuNjQwNjI1LTE5Ljc5Mjk2OS03LjQzNzUtMjAuNjgzNTkzLTE4LjA4NTkzNy00MC42MjUtMzUuMDgyMDMxLTU4LjIxODc1LTUwLjA3NDIxOWwtLjA4OTg0My0uMDc4MTI1Yy01MS41ODIwMzItNDMuOTU3MDMxLTk2LjEyNS04MS45MTc5NjktMTI3LjExNzE4OC0xMTkuMzEyNS0zNC42NDQ1MzEtNDEuODA0Njg3LTUwLjc4MTI1LTgxLjQ0MTQwNi01MC43ODEyNS0xMjQuNzQyMTg3IDAtNDIuMDcwMzEzIDE0LjQyNTc4MS04MC44ODI4MTMgNDAuNjE3MTg4LTEwOS4yOTI5NjkgMjYuNTAzOTA2LTI4Ljc0NjA5NCA2Mi44NzEwOTMtNDQuNTc4MTI1IDEwMi40MTQwNjItNDQuNTc4MTI1IDI5LjU1NDY4OCAwIDU2LjYyMTA5NCA5LjM0Mzc1IDgwLjQ0NTMxMiAyNy43Njk1MzEgMTIuMDIzNDM4IDkuMzAwNzgxIDIyLjkyMTg3NiAyMC42ODM1OTQgMzIuNTIzNDM4IDMzLjk2MDkzOCA5LjYwNTQ2OS0xMy4yNzczNDQgMjAuNS0yNC42NjAxNTcgMzIuNTI3MzQ0LTMzLjk2MDkzOCAyMy44MjQyMTgtMTguNDI1NzgxIDUwLjg5MDYyNS0yNy43Njk1MzEgODAuNDQ1MzEyLTI3Ljc2OTUzMSAzOS41MzkwNjMgMCA3NS45MTAxNTYgMTUuODMyMDMxIDEwMi40MTQwNjMgNDQuNTc4MTI1IDI2LjE5MTQwNiAyOC40MTAxNTYgNDAuNjEzMjgxIDY3LjIyMjY1NiA0MC42MTMyODEgMTA5LjI5Mjk2OSAwIDQzLjMwMDc4MS0xNi4xMzI4MTIgODIuOTM3NS01MC43NzczNDQgMTI0LjczODI4MS0zMC45OTIxODcgMzcuMzk4NDM3LTc1LjUzMTI1IDc1LjM1NTQ2OS0xMjcuMTA1NDY4IDExOS4zMDg1OTQtMTcuNjI1IDE1LjAxNTYyNS0zNy41OTc2NTcgMzIuMDM5MDYyLTU4LjMyODEyNiA1MC4xNjc5NjktNS40NzI2NTYgNC43ODkwNjItMTIuNTAzOTA2IDcuNDI5Njg3LTE5Ljc4OTA2MiA3LjQyOTY4N3ptLTExMi45Njg3NS00MjUuNTIzNDM3Yy0zMS4wNjY0MDYgMC01OS42MDU0NjkgMTIuMzk4NDM3LTgwLjM2NzE4OCAzNC45MTQwNjItMjEuMDcwMzEyIDIyLjg1NTQ2OS0zMi42NzU3ODEgNTQuNDQ5MjE5LTMyLjY3NTc4MSA4OC45NjQ4NDQgMCAzNi40MTc5NjggMTMuNTM1MTU3IDY4Ljk4ODI4MSA0My44ODI4MTMgMTA1LjYwNTQ2OCAyOS4zMzIwMzEgMzUuMzk0NTMyIDcyLjk2MDkzNyA3Mi41NzQyMTkgMTIzLjQ3NjU2MiAxMTUuNjI1bC4wOTM3NS4wNzgxMjZjMTcuNjYwMTU2IDE1LjA1MDc4MSAzNy42Nzk2ODggMzIuMTEzMjgxIDU4LjUxNTYyNSA1MC4zMzIwMzEgMjAuOTYwOTM4LTE4LjI1MzkwNyA0MS4wMTE3MTktMzUuMzQzNzUgNTguNzA3MDMxLTUwLjQxNzk2OSA1MC41MTE3MTktNDMuMDUwNzgxIDk0LjEzNjcxOS04MC4yMjI2NTYgMTIzLjQ2ODc1LTExNS42MTcxODggMzAuMzQzNzUtMzYuNjE3MTg3IDQzLjg3ODkwNy02OS4xODc1IDQzLjg3ODkwNy0xMDUuNjA1NDY4IDAtMzQuNTE1NjI1LTExLjYwNTQ2OS02Ni4xMDkzNzUtMzIuNjc1NzgxLTg4Ljk2NDg0NC0yMC43NTc4MTMtMjIuNTE1NjI1LTQ5LjMwMDc4Mi0zNC45MTQwNjItODAuMzYzMjgyLTM0LjkxNDA2Mi0yMi43NTc4MTIgMC00My42NTIzNDQgNy4yMzQzNzQtNjIuMTAxNTYyIDIxLjUtMTYuNDQxNDA2IDEyLjcxODc1LTI3Ljg5NDUzMiAyOC43OTY4NzQtMzQuNjA5Mzc1IDQwLjA0Njg3NC0zLjQ1MzEyNSA1Ljc4NTE1Ny05LjUzMTI1IDkuMjM4MjgyLTE2LjI2MTcxOSA5LjIzODI4MnMtMTIuODA4NTk0LTMuNDUzMTI1LTE2LjI2MTcxOS05LjIzODI4MmMtNi43MTA5MzctMTEuMjUtMTguMTY0MDYyLTI3LjMyODEyNC0zNC42MDkzNzUtNDAuMDQ2ODc0LTE4LjQ0OTIxOC0xNC4yNjU2MjYtMzkuMzQzNzUtMjEuNS02Mi4wOTc2NTYtMjEuNXptMCAwIi8+PC9zdmc+";
        cnt++;
        return likeMinus();
    }
}

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

// 카카오맵
// 마커를 클릭하면 장소명을 표출할 인포윈도우 입니다
var infowindow = new kakao.maps.InfoWindow({zIndex: 1});

var mapContainer = document.getElementById('map'), // 지도를 표시할 div
    mapOption = {
        center: new kakao.maps.LatLng(37.566826, 126.9786567), // 지도의 중심좌표
        level: 10 // 지도의 확대 레벨
    };

// 지도를 생성합니다
var map = new kakao.maps.Map(mapContainer, mapOption);

// 장소 검색 객체를 생성합니다
var ps = new kakao.maps.services.Places();

// 키워드로 장소를 검색합니다
ps.keywordSearch('서울 산책로', placesSearchCB);

// 키워드 검색 완료 시 호출되는 콜백함수 입니다
function placesSearchCB(data, status, pagination) {
    if (status === kakao.maps.services.Status.OK) {

        // 검색된 장소 위치를 기준으로 지도 범위를 재설정하기위해
        // LatLngBounds 객체에 좌표를 추가합니다
        var bounds = new kakao.maps.LatLngBounds();

        for (var i = 0; i < data.length; i++) {
            displayMarker(data[i]);
            bounds.extend(new kakao.maps.LatLng(data[i].y, data[i].x));
        }

        // 검색된 장소 위치를 기준으로 지도 범위를 재설정합니다
        map.setBounds(bounds);
    }
}

// 지도에 마커를 표시하는 함수입니다
function displayMarker(place) {

    // 마커를 생성하고 지도에 표시합니다
    var marker = new kakao.maps.Marker({
        map: map,
        position: new kakao.maps.LatLng(place.y, place.x)
    });

// 커스텀 오버레이에 표시할 컨텐츠 입니다
// 커스텀 오버레이는 아래와 같이 사용자가 자유롭게 컨텐츠를 구성하고 이벤트를 제어할 수 있기 때문에
// 별도의 이벤트 메소드를 제공하지 않습니다
    var content = '<div class="placeInfo">' + place.place_name + '</div>';

// 마커 위에 커스텀오버레이를 표시합니다
    var overlay = new kakao.maps.CustomOverlay({
        content: content,
        map: map,
        position: marker.getPosition()
    });

    overlay.setMap(null);

    // 마커에 mouseover 이벤트를 등록한다
    kakao.maps.event.addListener(marker, 'click', function () {
        overlay.setMap(map);
    });

    // 마커에 mouseout 이벤트 등록
    kakao.maps.event.addListener(marker, 'mouseout', function () {
        overlay.setMap(null)
    })
}
