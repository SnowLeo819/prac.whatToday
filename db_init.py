from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client.what_today

db.qna.drop();
db.ans.drop();
db.like.drop();

# 작성중 내용, 완성본 아님

doc = [
    {'idx': 1,
     'quiz': "코로나 시국 종료!<br>제일 먼저 가고 싶은 여행지는?",
     'ans_img01': 'data:image/jpeg;base64,/9j/4AAQSkZJRgABAQAAAQABAAD/2wCEAAoHCBYVFBcUFRUYGBcZGhkaGhkaGh0jHBoaGRkZHBwcGiEbIywjHCAoIBwYJTUkKC0vMjIyGSI4PTgxPCwxMi8BCwsLDw4PHBERHTEpIygxMzExMTI0OjEzMTExOjExLzEzMzMzMTExMTExMTExMTExMTExMTExMTExMTExMTExMf/AABEIALcBEwMBIgACEQEDEQH/xAAbAAACAwEBAQAAAAAAAAAAAAAEBQIDBgABB//EAEUQAAIBAwIDBgMFBgQEBAcAAAECEQADIRIxBEFRBRMiYXGBMpGhBkJSwfAUI2Kx0eFygpLxQ1OishUWY5Mzc4OUo8LS/8QAGgEAAwEBAQEAAAAAAAAAAAAAAQIDBAAFBv/EAC0RAAICAgIBAgUDBAMAAAAAAAABAhEDIRIxQRNRBCJhcYEUMpEzobHBI0Lw/9oADAMBAAIRAxEAPwCOvlUC9Va69D1vTJMtW6atRjVQYVyPmjyOoJRyKJHExmJoMmpTIpdDqy88UTyFSR94E/yqrh7ZprYAIiIqWTNwWkVhi5dsUjiWJxI8hRvDcU5OlgfWmA4VAJMVFFWREieu9R9dyWolPSUHtkL3ALoLrOBkfnSxHrRFh8GoZG01nuN4UISBcDGdgNvXlWn4TPKVxn34MnxWCKqUei1HFWoAaWgGpqDW1sx8Q8leRqQWRQKg0VZY86UNFotCvHEVYKnpoM5M8R6tRpqCpUiBzxS0g37FgWrEDDrXtgHy/OjrdypTlRSMfc94dG5zRiWo3qdt8SKruOx2Me1ZHJtmlJJEu7SuhV5+1BPbactRNvggYJNBpeWFN+EEqqsMD3qwcLA5Cq7fCgbD3q42eukfM1LXgcqZB1FVPctjdvoaPVB1PssV6/Cq2YP0oqjmAo9ojJ/6TQV+1wo2SfY/nTh7ekSWCqObEAD1NLm7U4fM8Uk42ad/1vTL8isH1awFRBAGNqhb7HuTJhfqaYLxYI/duXBEgg4jrvQ78S6eNnx5uY+u9dzpex3C2Vf+Xif+KfnXtT/8wp1HzP8ASupPVl7oPpfRny/uG6VwsP0p8ttQJJqB4hSYFUjmcui0sCj2J0tP0ohLZ6U3N1V33qFziQfhWnjkk/BOWKK8glleoosWxE1BXmrkRqpryLvwQAafDUxq3OKtUkCDAHpvUYkwTFckgOTI3bp0yaDe5mVkedOLduBj5mqr3Dljg/y+lPCcVqic4yexQZJkkk9aki07sdlJHiJB64x+VB8RwWkmDI5dapDNBukJLDJK2CM8RgGrVUHIod7RnGaLCwnnVeROiBuqPM1aL4zkAxSwgipB67kgcD08S8k6qItcS0Rqz1oWpBc0rmh/THdu+sDxCfz/ACoDiBcuvCMYj+W/rULXCM2dh50WnGLbAVILdeQpJW/2hilHsYcDwJWCTJjei3twJJAA5mkf/iVxB4Gkk5JyY6dIoPiUusSzaiPeBU+L8uh3vaGr9vBGKouoDnMCfLyrrX2iuEwQnvOKzqAztVpUzRccaQUps1nE9uotsaINwjeMA+h3oDhu1+IJksGE81Ee0RSvhuH1MATT7h2t220TJ5nkKxZsigqirNWLHf7nQbwHHX9XiAKGDI5Y860DcUgQuWhRvNZ3hbLu7OGhR4R6daG7R7NuuDquHQM5Pl0rJDI5S2VyY4paLuP+1yo4VLeocyW/lFGcf9pktorAeJgDEzHrWWt9jamnUI2B5V6/YVxjCqSBWn1MSq2ReKfgr7b7buX4DHwYOkbT1686TlPKtCn2Xu9I9aYjsC5EYA/w0/6mKVRQiwW/mZnOzu8VhpkdOm/PyrcWOENxPHbAwMAzPn4s0FwvY5Qgs8gfdC07t8SqjAM+n96zTc5vfRZcYL5ezO3Ps4xJg11aP9vP4f1866o+lL3H9d+yPkwVjuxq1ek15ZtMx2imNqyB617EcVmGWagVVPSiEtvPw1dqAycV6eKVRJaqemkTeWTPUst+GpBG86FTj3uHwGBtmufj3AImT1oqKQrbYbLc6qa4pMTBoAXCdyZq1B5UbSGUWwp1O5J96stcO3xAx0nr5TQCzO1Mk4uQAwyKlkyNdFYYvLKeJQqRLk4BqkMTzNF92rtMT60YnDLOIqMvieKKr4ewK1JEbAbnrXOCaa3eHBwdqgOGAroZ/Ik8S6QqHCat6pNhBzn0p3e4UssDFLh2O4zqp/WXkVY34POGSyPiBPvXn7QoJhVA5df968bse5yk+4qSdlOD4k+td60Fsb0pPTK+I4/UmnH50CFJOxNOv/BBvtU07NUYLUj+LSXypjR+HV7Yv4bhpOxp7YuoF0Eb1C12ag2ZgfWrl4YLgHPUis083N7LrEorRV+wWswsxmrF7Otfhqy1w5X4SJ57VHjOGu3GVdaqBJwM4gch50scqfaOljfhli9n2jtbz1n8q5uy7ZMhSDzrxuzPAQHMx15im3BIwQLvHMzXc4vwK4uPkjZDKNIUx/hn+dXpw2r4tvMVVxXDs2O8ZREFV/rvVvCW9A0hmP8AiMml5JaSBTe7Ll4RB0HsKsVVHMfr0qtknBgj3rjahYED+VTb30d32whCvI/Wh+MvFR4ULny/rVOmM1YlwbEn51znrR3CtgHFcXcCki0Z84/KSan2brueK4iAcomfQyB9KNuhYk6iPLP0qFm+pHh1e8j+dDm0tsOn0gjuE/DXVV+0jz/XvXUPUQvCR86WDtVgSs4rnzq66SGiTyI9CAR9CK91yMCgPtE15+xId1BpPZuH8Z+tXjin5MY96RyHWML4nhWiEVVHM4Hzoe32eebqfSoM7MZZpoi20bn6VOU2uisMa8so/Z9JMsParkvR1q57qxAUesCvEj8M0vK1tFFSemcOMjaPkKmnHDmCfYV3dj8NdAGIj3qct+CkZV5PX42cBdPnz9q9XjAMVEIvMfWibPBA5C/X+9SbrwPa9yP7WWICmBTbhruOtDWuF8h+veiktgVN2FyiErdr3UNyPpVSL6/SrB6V1k69i1bo6VFXDCfM/QkVXdcKrORhQWPoBOKX/ZnihctGVhld5zI8TFxHswHtSuaugqDqxqSB5VUyqfOiBp8qrNtd5oerQeFlSWMzifSjraD7wmqQ4qYueYpHkQ3FhB0dKClDcaBsq7Hqzz/2io8bfC22YlTpUmPQdaX9l9oW7hZgQpOlYJB21bEb5LfKleSKdWOoSauh0APxVE8Rp8/Sqgqc2qjv7WqAH9dJijzXuDgw+3xQPl61dw3ErEyN2+WogfSKWXXUAnJABJ5YFT4S2uhdUzpE55wJpHKIeDaHS3Qf96uCzSX9ptriR7DPzo7heMSPi+czR5Epwa6DTZBqg2DJ8MDrP5VevEL1qviOLC4iT9KeTxqNuSJrndIqucN/FFVM3INnrE1VxN5zBIEHZf8AbNB9y5k6YHIZG/qawz+IinSNEYuvmYZqP41+X966krq0nwCvaT9RD3K+izJHss8iPnUbXC94pgjVbZrbZHIgg+catPstKrdh5AZlWYO5ODnkNwN/50AvHXbb3Ft3DDEzBMNEjbpv869mWWcq4voyvFGC2uzUL2Y3UfMVI9nHqPmKzj3mYYuXV8xH5yN/Kl73OIO95j/mj+S07yTXlCKEH4ZsDwhH3h8xXo4X+JfnQXZPBPctC4WMgACNREqYOrAmd95zVFzhLiFf3bZJ067iguRnwiZI0wcefrUYfFuTkvYvL4aMUnfY4Thh/wAxfnVotL/zRSdOznIQu6IXyq6ywZSpIYaJPI74PXlUNfCyA11ieegQF3IB7wg7R/en9WXkT0o+B8q2/wDmD5V6RaH3/nSFX4dhClnAaG8SyFE+IBRMb51D+dCuEZhbtsMkQdDiT4oy7RzGT+L3pXl+oyw/Q1avbH3ucVM9pJuLmP1yArK3OF7oMbgmGImCAGABgw2+efUxIqL2VzhlJMACepEDBO4Iz0pVk5eRnipdGtbjgf8AigeQAGPevTxv/qD2isRwV1bjFQGBHKT5b8oABpk3CAG2vwm6RB2HiOOpMnTkSM0HOg+ivJoRxSkgd4xJMATuYmB7Cr7/AGgLQh9S+Z8yBPtM1lbJGW7sEhgCCQYIYcgfJhv1zVK8MbYa4pDBzp0ElgCDI32BkCP4DU5ZArEvJouL7b1I6QfEConoQZJ6VDsLjxbtnUI33O5UY5c9vehO0LS20tkxL64wBEBCPPEkZoS08W1gjd9z/h2pJJ2Xgo8dD6120LaKpAws7ycsREAb899qbpcuModAjqZggtyJB+75GsMt9RONWBttGM+tUvxBV1YM0W3kQSI8M4jbJpHALSfRvg90/dHuWH/copdxfa7W3ZHEQoOCZJM8yI2ArP8AHdtcQRbi64IIOD1HzPvRo+0HEAE96DnYhc7422zS8F9QJP2Rd2n2yG4dsQTiCRgah8U9RyzvWb4Th3t6WDEFhqI1eHIMSIzvMzzptxXa9zjdPDsVjWhOlAIzqOfITjyr3j41tCmFJiF5L4fliqxcYpx7v3JTUpSTWvswu19pAgi4xBgAAAttucCRRdntsONSFiNp0x/3EGseEZzscyQOW0Yn0j2rRcNfsW+DKukXQHhgxySxI2ImByqE8UbpP+5pjJqNtX+AvtDtWLbfEdXhjb4sdTRbdo/in0M1g14+4UlpbJAEmRzkedOOwLpuXAL7XESDnmsAxjSSZ8I/OhLDS7Cpp+DS2u0E/h+Rpha7QH4h/wBX9KBbszhwyInEMS8wdKlRH4toruK7N7plDX08Rxgz6kLOPPapSxyW/wDZyljlr/Q4HaIAkmuudrqQDzzj+X51nuMaCq6kbf4ZxyzqAql7smOQGP186m8dx2d6UGzV/wDirMszGYwR+VDX+1Gjf6if60u/Y7gRYSRAOGE52xvS/ibN4Se6f2Un8qyTxZJO23/I+PFh+g0/b/P6/wB66s4bV3/lXP8AQ39K6h+mfuaeOMXcP2ZbLlGMPAOkxqgwdgJGCDkdKF4/hhqcAZVv+nb6+E07+01ko6cUhAJm3Lxp2OkkKTJjUZO8rilNh2uqxuWyt2ACTgMNIhgAI3xAxINfRYPiI5cafk8DJilGd/8AUBtR1Fc8RXi2rYObSn2H1x1r3uwMi2ucbDn6VVgSp0aD7M3k7t0ZwAGBEkZLDYdTj60PxiFbxY3GKBlKgztgws7ZFS+zB03SMQynnzGf5A0T9omXVIMsFAYAbEEkfQ15c41mdeT0sUrgrKu1O0uHtvbbhlKkhwxEAiAunBBAETgRMGaxv2stnv8AvHBm6qv67r/+tMOG4V2uKXH7tmJXJk4PwxPPGx5HahvtSC3dMIbSHQwRuDqgkGBAP0r0MceNJf37MUlabZR9nb2lrixkpqAgQdLwRt+FnM/w+dO1uFYIAwenMEf0FJuw+AuFhchQmRBYSNxCyfh9SaaM4J3jVJAxtjFDLErhnqgrt3jri8bcUOe7/djSIyjBSQQMkEzvRN6wodn7p2XxM4hgAQSNQYDKwRM8zvQXb6xxFu6CCGtWg5GfEpAYecgn5U+7E7QTueIUAgMulV2yYGOQ5mpQj/xqS7SR05tS4+7FvZnY6Xbjd2LltX1z40IVZ2A0z/DzobvPHbQvqNtQIIEDRcRAPWAM+Zpl2ce7uC7LBYfcyB4W88/Lp0rPdr8Ndt67uqNTjKnPj7wweW69eVNTbavQeSjTrY14zw8abckg3GJE9NRz1wZo7jLA7vBCkXLbSf4dc7T1pTburca3cKwwNo6ubEqLbT66tzTvjrJa0QDmdUZzpEkCBvSVTX4DdpgXEcW/EBCVH7pnELzkRkycYqk6gNJEHcchBBBn1B39KX8Jae4lwIGaWJ0qCcS3xRt7dflXwhNtka4pK6mGiMgoGMEAzOM85HlWhRT7JuTXXsP+B7QZbaBUQiMEpJIJ6z51YO0rh/4dqMT+75eHz5ajVHDNbNtGKgAhev8ADG2N6na7sbBY3yGmBoxGqOXnTp60SfZTw/Co1tVBJ2aYGqDEbzAxVPavChbcq5zAAbTIImcj50Fxt3u7gCfDpkZ23FT7q7et94SoRRmSfDkiTH3T1/hNZnGbknejVzhHG9bHP2euW0uPcXKKhgtE4HLz5UFxNw3FBgzuWjqBA3+tXdlcCRae27orOZDHYiBgNGNtuYyJqPGcM9tYEXFAybZkaejAjP8AanjgaVtEFlUnSa+xRbssCTOk5Gce/p/Sp8bYcoAPEecbwJ5DehX4vu1DkHQdmBBWZzsPp617b45XUqjBjicEQCYMYHKanOD5Wa8c1xqwhezCSHW5bgqBBJBBjxAiPxTHtXcRxDWXQsVYhNI0Hl1Mjel7cUwnLRrIAAGPLPmD86L7KVrtwJLkzCzsHz4oXyO/IUs42tK2NB729dhzdqTpAD6okhoxkzMZE4G3Or04oPEE6wDiOkxHWk9t4NxxnxJbBicKPF5xIU1LgFPeaBMyQPMidvLFTjjvvspKdaQ/KOzYUzzgHEdaEDMjEsJg+x/tU7Fy/bDKWZZB+HqcZyfKg+PchzI32Jg4HTpzoSi+jovYz4TtUm8GaIQ6gIMYinvD/acl8qNABnSsmeWSRjc+1YfhuIIPhjUf8s899j70c5uAj4euSMj/ADGovHJS10M8cJ/uHvHfbbTcZUtyoiCd9hM+LrNdWNu2rkn92Ou68811PwfsD0IGx+0fDd7wt1CsnTrAM7rBgf8ASsqxrG8R2rLrLSzWyCJiAG8MnA31/OvoiKPYx0zPMxiSZbKivmfblvuWddOFYrnoZKg8jIzHn8p/AtXT7W1+ezNP9rXh9/gtInODywZEjcSDnM/KrUfkVHuT/vSrguPBU6pWMnUf6gQPKiG4q3/zE+Y/rXr8bWzFJpS0MbV0ggeEDaYz0oz7SX1UC6SYKqTH4sLHzilI4pMQ6mc4IJ+m1W9pXjctMiqW8JO2xwcczkDly5VL07kn9yiyUhXwCajq6ksuYyTIknHWm/D9nl9MMoMwDqUg7YEHNKrfZ9xbGqcwfCCdQ9wN46UvHHLGkaweveN57A9KK29DN0to0HaPZptZa4sriA8D689/l6UqvcSNSASMHfVmYyOdBrc1ZAJbzM7CAeXTc0Z2X2Q146gwWADkeEknAk8zE8ximaQqkw3heN0u2tm3WNOrbYjwjJxt/Wm/ZXA3kDyBBQOPEJGnJkEyDpk0Ld7JNtTdfS+jS2SQJJIGFj135jpTLguMVrwcL95S2B8M+IHqIMUkpJLQ0YOTtg3E8RptlicefLU0R9YpZ2jfVmXUFZShBkAiQcehEnzp1x2m413UAbTuSxmPCxHhzuR5UlTgGIuW7dtQxUEEbxhh5TyJ5SaMU6+4JS39g8JbJsG2ukMAzCfvW7pYx0HhWnDcRpnynr+VKuzbbWltm4gnQwEwcFmBkT+j70Wt1fwJOc6VnamjiT7YJZHeivsebdtAqiRvqKgySSd4MZrztKy1xlfKshJAyRBUg7bQCfXyqriOPCG4CB8Z3jffHTlt+dRPa823YgDSCABMfCQCTEfeODvnrTqCb2JzlFaVkrA0W0tnV4YBgf4OpxXl66otn4p0kyYiNHz5b/SgeDcucGdTHBUc2XYneiSAG0tjkcAYAeYODy6VZVWiMpO7aFBbWsBvY7R/XYe9O+M1cPcZVKzbUL/CQACQRzG9R4W4jXFm5LakUDTyLAb9c/Wo/aUnvLtzkxb5jH5fqRUOlv3NC+Z66qwBO27gI/dWsbDVd0rPQF4H96Ksfae8s6bdgT5P59WpRa0keJ7Z9TcBHyWKtZk/9MwIEF8fQZ8+dLzfQVCPZ3HdpOzB9KWyZnutS6v8Q1Qd6J7Oum4rNJIB2LE7DlJ86Sca+RtgHb+e3lT3s20UtBWBV5J+ZiD0xBpZdFYdkojVpYzqUnI3IZiDNHcLxi2wdRk69SnUAwgT02M7eYml3BW9THaGunPRVZY+geu4HjLZKi5aVgxtgQSCvem4yyAY0i2qcq6EW3aY05pLaK+N4kBvA2JZiMAAneIH08qafZZy7s7T4AAM4lpz6xj3qLXrMBl4fvUYAqFL6lB/EATjfMVLhOOCmUtd0DlgxZtoH4ZmPOKdRjF22TU5PpFfavHsLrqrtAPX6CPl7VPiwTbQzqY+e0mIM+o50v4jhWNwsDqBMkwViTOdXLO9aTieAVkUMrbYAMYwZlVM+s8uVZcskjVibsy/EyoAYQd8/Qzzq3ibj2wlsXBEaho2ydmPPn1oS+5N7SA1zS0RMkhTkZ96H49yrHwNbB2VpGPffnTqGrA8u6DF7Sfoh/8Ap2//AOa6hbSWyBPEKp5iBiupvTB+p/8AUfVOAvh7aNvInHSBOnM4GlZUkb4rHfb7hjOsTDAnG2tInbG2lfY08+ynEyjW5nS2JjY5WdhgGcwcDNS+1vC6+HZvwMpzuBtB57Ekhtsb15kP+L4mvr/km3yhZ8t7E4mLmkxzjEb55b7HfrWhR/IHegT2YmoIC5do7sJbDAZBJIQkzjBxid6le4Y2W/fuyoZAKjJMSMasefy3r3GjCpIvvcTpGfaP7e9W2eAuNcDHw212PUYJnUBII/CJx70w7I0C1rZmUsWCtc8JgbG2tzA33id+UUfw/GWwVU3VYSAQWQlhOZjekTjbseUZa41/Iv4ZTqcvqFtmSZnwnwqW22LfoUBf7MRSwRj8Rg6pEDptg+sbbzWpHH2O77s3Laox1ELpE+KZ6bjl0qhOB4S4xjQ3UiCQJAGBnmPLqRU1FbbaX5KSk3Spsz/ZHYzL3jMyOisqr8LeIhp1LkHYgZP8qZ93bRbiKpXWVd4wdWBicRjpzND/AGs4NbD2+6tkKYwAeWkyQOeSNh8McpNVtPiBLHMctjuPbFI58o2Vxxqf4D7CoSLZko5hgzDkGgAqZ6fWk+nS5WSQjaZ2kgxPPOMiirDlbgUkYZD8yP6mqb3ZIe9cZbipJJ0sCcsZnDSMn2naugrYZvirKOJvhLxBiGj2DY5t1BNP+xeLRrZyY1sDOnO0TIyKQ9q8WtuLTKHSUJAJGpgT96JiQOXtV/YHE2rzvaS0EABbNwsDBVTyEcvrWvFC2kYc06TY6+0LhrltVZBFpRBMczsAI60uD6SVZkxg58t/Mc6YcfYDxb8CfupQHB7wFgAfLEc+VY5+Mu27i27ilQ/dagcFlnQfQHxDblTyhxlsSE+cddmi7Y7NTSbnexlj8ESdGpVgc4ESczHpSfse29xWQLu0EESZgeUT6xmmnav79EVNKKrffuFVmI30ROdt/lQ1ns8W/iuL3gJYFdWnwxAxEtv15elCdN/KPByjHfYbwtllZi0qyqWAGkCTtsSScEzqM85pxwbgFLhuFZUBpEkGIJUT4pI6Yk0h4C8wW/raZURIgYD7Zk7+tME4d2EhhjaWgjPLHvXRmobFnCU9eRrxdtHhkdtedTMjAN+GBIAOIisz9ptS2z0dtXo2zDyOdvIUx4dLjtHetgjdzGNo6/2pd9oGZAiNcJLPvqmNpI9etDLkjOOltBwwnjk3emqM9YtAzC3CRE6VED6+tWvbCfEtxZGNSgT6f2okcVdWUtquhTCluYAkZkDYT9N4qm7xRYN3oUECF0gyTq5HKwIM5Bziazpts06AQZuKvVlH1H9a0qvpZiSSABjppEn1rMdmtPEA76STnyBG3rFPjcBERuwBPkzBT7aZ+VdNDY5UWKO7tvBkpbfOfjPeKP8AqYj5UHeITX/CLsRvpVU4ZD551mrUvgiW5ujHyAm64/1WT868sKTAbJBtF5ySqDvrsET9+4s8jI3MVSCpC5J2yfCI3erbRmBa9asypzpsqFefLxA+1XcT2i7m6bYWHvC3aAUQFlj087X+qqeym0fvCfFasXbxnbvbphM8yQ6cvuiqLN0L3U/8O0947fG2LZ+ln/VXSFiwx+0HYubZHivC3ZMDABOo7bmbUnzNEL2odF24oBTvCqgqIAAJJEDBM2zOedKbT6QkTNqy1w/47saPkGsn/L5UbxPB3Dwdq3btOTi4zafD4sjI6DSDIG1RlDk+i0cnFE+xOFUW+8dNTPJklgdM8sxmJyDvT201phpNwoPwugYex2+lQsi2qLbK4VQoZd4AAyNjVN/gTGpDrHVd/cUboVSCv/CWOVZCOXgWupP7j/UR9JxXV1Mbn9Bp2LdKXlnZ/D9ZAznJkRkYrY9pLbW24uNAZWHz2gbnO24Ecq+fK5EMNxkeoz+R/wBVPB2i91FLAEkcwDpJGYPWOeTttWXP8M8mSM1+SUMijFxZnjxt2zc7sO3iUxHMQd/daAucVdLg92YBnKFvLOpCJ32j6037b4B7oHd6CwBJDnGkxnnzA/1Gs3+yujFXNlQFktnIzIUSC5xsOo616EFrRCUk2rH3DK2hi7eKQYIkhdhj7u+30FdbywgmeX7vpXdmcYHZ0S4hti2AAAwcGVBMHBGeecR6+gwSdVyVz8iP17VOSqTLxdxTRZcToW8JOyDbBH8yfareznIeJfKtuoAkCQZGxkCvC3i0+OCOvQlf+0z/AHqqwdLI0XDBBMttDbEen86WUR4SGnbfFOLcoSDgei+LbODDIP7iaRI4USwMidRjEiQeUY29qccfYZ7TqoJIVjjpb3IHL/4Y9M85rH3jmSJBHJFI54yfI+1GENCznUtGg42wrsLls4UBQJB1KsnUYMySQBnPOl3GIVYsY1J8Wx1ACQTHQVPgHY23tjWhHMqFCzgkBYloiOecZig+K4qdQO33s5M8iRvJpuIqm3oF7Sv6xcgbaST0UEHbpv8AoUX9nLbWwL6iFdSoz+Fxq2BOCkZ/EKYcN2cABcKmGCPKlMmFjDBjAx5yanwV06QXlYa5uVBCyY1aRp1QFz/tVNxrwyOslrtBnDB7rfvXS1bPnDY+6A0bzmBsaD+0nZquUfWzC2lxpAUqdJSFJBEeKIEGZO1XPf0z4t8ZCsCMxEiVMcxUb1g3Vty6hQGjceIEknYciOmetU/dFN9k0+E3FdAXDdsstu2iEKhZjAGQ25OROSI577mM2cN2kt4p+0fDpuFAEBGoMAGeImIB2zWcHEsO7V10kOxyIYSAfUY6z5V5avjSpJIgNBAG5c85Hn7gVLZfRpX4RSgG5PViASQROnTIODz50+4N7YsZulW/DqOd/wBHyrNcPxVx7cqCVVRJj8QYfh5jT+t2S3lFsqwGRvqYEDHIdM0HE7mwzsB9VyBcaBnc5ExPgHLEmkn28cC4q6mJAkSDkzBkkgrAGMH23ovstm1krbNyP8RgmcwBk4JjyrO/aYM91VC/CmRzEk8iRNLGNSDJgwuSs6tIEdZM9BMH5ivUupoJJZmmYIhRJM5DyZ9BHnTjsP7O98gJD7wx1hYYZwueRA50zT7KLABtKpB+JrjMG6AhWkY35eVUUNC8tmQ7FZdbPmApmf4unnAMU6bChcQZho/hK/RmWr+O4Du2NkldJ+ArsrkAm3kbHBH+9LrrYgdIE9WJIn0KLSS7KR0i9/EiqMaw3IYN10t++9361FnDBjBOpbhXqGv3DbVROI7tSY6VWb0DUPurqE9Vtm4P/wAl9R/lqarD4E6HJ/8AtLQC+xdmqlaJcrYVxJmzd0DN2/bspndbIxHqe7qPFcNqa6lsMNdy1ZXwmdFsLLNnwgA2jPQDace3boQcOpXNq0b55eO4SyggdT3XKZoJWCBcn91ZLz/HeMKfXS9s/wCShJbGi9FjMLhMYW9d0jlptWvyAcf+3Wi7O4+4S0XCFOrwjxDTsBJHh3GAeVZq4TJBObdpLQmB47oJIxzCtdX/ACCnf2csAW2Ygyx2I20zsJ2knJ6YpFaHb0MHOd+fzqAYqZGD5YP96sNsYP0/25edQYn28xj6be1Gidln7V1CE85XPvBrqpwP+Z7CR7HnXUvBDczw9N/10/08h8Vdw3EnKRgbHqOmJAnHXbbnSy12sdu7joTMD22EflUy+nxOTPQc5/Lz29d6dRZJtBPHEuIUicmTsT55yJA58t+VZS5227IAbVpomNSGRP8Am/UUfx3a5tlW7sXFnbUQAeU4zOflQD9sW2knhkkyZ1tEnyA28qolSJvsn2LxhYXDChowVAGNjgY3K/OtQjhgHLt4lBjpqAkbcpPyrN9nX9SAi2lsznSpEhhvJknIPPpTnsviJtm2d1LAf4SdR+hb5VPIrNOF6aZYjghctvpPuNOemw+dcWDSCHmSwH+JZjHpXmpiGyOvpIk/VY96I4Fwb1uWwTAHnuPlIruN6O5Vs06cQEBDXVI0rAkKSBgySOZB3NLOG7Itm47LoUsCQygsBLElQpGhduRnGwmjLrqwk3DBAM60iJgkHyJ39qjwlsIyy7M0sPEykkiZE6Qec+VW4JbRleRy0xN9rrAs3LNwGWu23ljuSGMxmABqAA5VnuzuDS4Wa4zACICxJOZOcYGPc1sPtlwhuWLLif3dxwYEmCur13A2rNdp9kXLaDu3AJEtqKiANtI5g+KIkmB1qfB9lecaS8jLggCFtqCUVWDOcEAKQmnfUZEHI5daSDj2UAM2SCZODnVtGMflTHgEctatkG3bS2Wu3DiQSGblEwFAPrFMF7K4a7d1Wy7gWwrAjAk+GIAMwGmZ3FGUNpeQQnab8L6iL9sFzHOdpjUxkRnnmrbN67cYWkdbdppB0yXyviyF3J6eVFn7JxrdnGW+EqYOuZgk7AE/6eVWW+xyLdtNKEqT4leCQcIvjEDSBzOcedd80dB+Wbsz9jglvXwW1C34S0HILW1CyT1YATnbNWcF2atq6tu+F05kEgxIJAlDiTVXDOlu8iksukuLjK2CEkKCAZPL/VTfhXtNeQQHlCWbbPjJwBM7DyoppJNglGTbS8qvt9TuLPdN3fd6E+5IKmJzBYgnMj6Vc/G/uyhRCJMGBqE+cT0/lzo3h+DQS1yLjFmiSdQmcxk9NxgzWcv3csAxiT97zkfr1pJfN2PFcV5/IfwfFMmVaDj6eo/lyqm/2aO+t3zc1B9KlIMiSFg8vhkxVfDglcGTMbnYSPyFVXOKciQupLeuGgY0A895wK6qCtsdjiVtqNNwDVGFMZJAkxthYzTA9pJCSw6yT5f3oC7wFsWLZeCwVfD4wWmBJKnEZ5dfYReFt7C0J6m7d94kZ9KVtrQ8WpX9NbCO1763LdwgZncETh0GqN4An2BpDc4vUwBVGaVUkkwzeGSY2ywp5xPDpbJQXA4KvO4wA+D5zGcVmXtMjF8+EO4OPiAxIHnprlG3s7ncbX+KCO8BbV90sG/yNce8ffu7VoeWK60puAJnW4s2p/ivubxPtge9ehVK6ARIJRNU/eK2QIG4It3PduQYxbwN9Rd71Z021v8AEwfTu7a+zKIPQirLZn2j3tFzcu3dMDvbqWEn8CQJHl4bR96qN0XDJwl26zcsWbInPszf+3VCSiKNS/u7dy6SGE95d8CGf8LW2HWDVdzwhkX4kt27IH/qXCXcb/8AzF9xSvY8T25cJVdQ8V1nut7sVWOuVu/662fDp3dtE6AA+u5+s1luyh3nEaBlEIjmNNpdEjpMA+9ay4frSpbGkzzUPXyrxz5Ceowfcc6rUwZx7jHvVmqRJjyz/I1zQqZ4pH8Pzj6TiuqtmXmRPOUz711DiHkDXey2tWyzPb70A+DSp8QMwJjMfXNJ+I4mcnEnc7cs9T0+dM+3uN7sAAanDA/78vPPMe4ZcABctBbltVzrJVztB0kssZztJ/Mcp6cn0BwppLswr9rkEhbt1eoAQifeK8vdquVI71zIjNtBPoQZHyNEfaywO8W4B8QKtAG67fNY9h60kJ5Afz+eKqpWrEcadGh4V3a2qhbjNqJh5LgQgwYHh9t/WrOAOl3FzwHHheQSIYzuOR+RrR9h9m2RbRSxceFvFM3GMEBt9Kg/dHvOah28gFzWdDsEEqVA1sG2DDxKAGiM4G85ouDq2IsiukA60mZTnnUes8z1qKOBBUodORDdM9a94bss3IBJUmDjICwCQBuWmem4Ec6lx/YD21Ui5rLECDI3nYyZyIHXf1RQk1aKvLFOmzUXL85DbzHjOxGpeX686qbiDIM8wd2O4zy8v9qSJ2s1u3aUKGYKNfiMALKr8xB+dQ4jtdwitqtKTPhLuTpVjOB947QY9adyXRBRfdGuvqbnDXVUFmVrbgAxzg/SsdxV5iC83YAmJA25yiiMRWk+zHaneWzcIibRYgdVg4+tZO5xNt1EeDvDpAXxLERuDE5EifPAOFlJ1opGK8j3s2xd/ZxeXvSWfYuWIXS4kav4iPapvxEsVe2ZJnIUGJb57AZ6Up702rzWluNpWYUsDA0AiAWkbjlXXbpNydR+AmZ/CLiwY82HyqjdR8mTG256Wn/If2r2j4LYEoBOAFYiVQCNRE/e+dL7fFKRr/e6fxdykSZnJMctvKr7nSDIKHBg4LDHhOPDGB/Wq+O4s9wQVuAW4YsXOth3gGSwiBrPLYDpUJO2boKhRw6ixft3dUlxcchtKhQYAnlmRv0ppxvbi3FUKB4WmQyjJGkglTMZPzFK+1AoBbUzHSqgkBSCWJaNMY0hQOvOhOxlDXFtuAVbcc5IEH4oIxvGKNX19huVLf3HA4pyheTpXc5iQDgkHGD/AL0rXgrrEkITlj7T5fL1jpWg4myLdi+tvSbZILay2DqA8pER9fSmHZb2zatsLQ/eKo0nIC4OdWIET68qHyw2znznqNN/4Mqtu5bBLJsZk7iY/Xzoj7JI9wXFDKB3ktO8NIYIScHApr2wVRWvxAVdARQB4tMAjOwKg/LNZzsPjNHeFfCHOpZ6Hlg9fzoqSatHcZL5Zd0artGUUAEahpUCfu6zEnyBHypUbzDLC5iPvef+I/rlUjxSuJfKhl3G/jII3/UUE1+0Z8KqcZ0yZ1Ax7iRStWx06Rf2hdbvdNtC+pCDGI8R658j60Ot4q2oiUJByASRILKZGDAX3n3c8JwoZwtwiLikEE+KI1EDHIx6fKvO2OGt4ChtVxtMsdiSciPPGevpTRja/wBCzk09r8mcu8M1tiVRnRfErEEghLfgPh6tcYn3q1nJt3FmGuXLPDBhM/uxrZsnMvo6bzW34m8qsEMIAAohhPhgK0HYQPMGIrH/AGg4fumUoAEQXbmDMXXIAHpPdlZzA8jVZJRdJ2Z4uUlbVFRvI5Ja5cK3LhPl3VgEkGTkFST5lKrfjv3alnMrr4jTp8JdmKoT4seIhog/FyoAqQpUCCEt2R/juku3pjWp9RVXG3YUkbO2hTIMpaXSPmCvus1NoqmP/sdYhWubSQin0gtn3TbpWkZJ2weYHPnI6/rlsB2Qnd2UtkfdBYeZyT6gk0QwIOD5gjp/WhQrkW4O2Oh/L+fWvGQHIweYj8uYrxmkTz59CfTr/T2qpngahy29eUe8Y6A11HWRbjnXwrogYyATPPPMTMeUV1Ba/wBfo11AfQs4XtEniRrII71QQVB3I574mtDc48oGt7sH8A6lzgE+siTyAryupJQTlGyik1GVC7tHs8nDM7EDMFQpYZJAIJxkDUTjzNe8J9nbZRn0w0EgliSCwISAsKPFGOQ5iurq2YoJ2efmyySQdwGm3btuqkS+i4pMxI8EcoB07UJ2/wAVB1QCdszieYgjPrI8q6upJftKr94ps9pkMvjIMiIECRnYY+dafgO0e9RWUkusW11TuyxqJO50/IauZz1dXY+wZ0uP8Czi+xR3gUMwLbYB1EASdwBvPvFIftBwZsuqyWMamwBE+5mva6g0rY0ZOkaH7D8cFCapIHehh/DpY/yNUvaV0QBmWMhZGo6ojV4NPwjOeQrq6hHyOz3jLTWRautcZzcuOkuc+BlA+EGZDc42qu7xEuux8DCN51Mp+8K6urpE1Bci3iSxVhB1YMSNjcuxHLnVHDfBdR+dtpBzvoIMyZ6xyrq6kLRKeD7BFywbrXDnWcbDQTyIM7HpSfsS2y3kaRImI3kqwAEgjfrXV1aMsFFRohgm5zlfgc8bxzXLN9WADKFjzm7DloABOBy9Ks4LjnFkCYAAI3kcuRjlXV1ZKRt5O/wT4i43EWms6iS15ADJhYR5wx29PKllzsu7bGpVUqWZcxjTI2nmflXV1UglRLJJ2PuE4Sy1hLdwlX0PLAmBpeW5GcnGKot9i2VcksxhhogzMSfECoHT5/Lq6nT+gld7Cu1eM0BFAGppyZxJ5EbHMc96D7Juu99EcqfFq5zC5A2joa6upcP719w/EN+m/sO/tRpULdMyvhMbkMZA36qT7edIrXalk6g6udcScSYJIz0kk11dTZv6jJ4P6cQa/wASr+IL8TM3KdZAXXtuNx50COALm1MaFgAeS+J/ckk+9dXVJGmXRpLd2f19POprdHsa6up0Z2SL7D9Z6EVTxtw4HufXYT1O+f4q6uoM6HYH3g/X+1dXV1KUP//Z',
     'ans_01': "도시의 야경을 감상할 수 있는<br>뉴욕",
     'ans_img02': 'https://pds.joins.com/news/component/htmlphoto_mmdata/201611/23/htm_2016112317410723403.jpg',
     'ans_02': "다양한 액티비티가 가능한<br>스위스",
     'ans_img03': 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTW4sgXzHvnlyfrpaPIx1kg4Qg8UcoD08S_zg&usqp=CAU',
     'ans_03': "우아한 만찬과 낭만의 도시<br>파리",
     'ans_img04': 'https://media.triple.guide/triple-cms/c_limit,f_auto,h_1024,w_1024/64cb56b3-f09d-477d-8827-66f8a2d95705.jpeg',
     'ans_04': "바다를 보며 휴식할 수 있는<br>괌"},

    {'idx': 2,
     'quiz': "즐거운 여행을 끝마치고<br>집으로 돌아온 나는?",
     'ans_img01': 'https://img.kbs.co.kr/kbs/620/news.kbs.co.kr/data/fckeditor/new/image/2021/05/07/314691620354493423.jpg',
     'ans_01': "여행은 자주 다녀줘야 제 맛,<br>다음엔 어디를 가볼까~",
     'ans_img02': 'http://news.suwon.go.kr/upload/article/201107/8968753924e33b7ca82c85_gd800.JPG',
     'ans_02': "친구들에게 여행 썰 풀어줘야지,<br>바로 약속을 잡는다",
     'ans_img03': 'https://t1.daumcdn.net/cfile/tistory/99CD794B5C64CB9806',
     'ans_03': "사온 기념품 먼저 정리하고<br>밀린 집안일 해야지!",
     'ans_img04':'https://img.huffingtonpost.com/asset/5d8148d23b0000039fd65a60.jpeg?ops=scalefit_630_noupscale',
     'ans_04': "돌아다니느라 너무 피곤했음,<br>집에서 휴식"},

    {'idx': 3,
     'quiz': "갑작스럽게 휴무를 얻게 되었다!<br>오늘의 일정은?",
     'ans_img01': 'https://s3.ap-northeast-2.amazonaws.com/img.kormedi.com/news/article/__icsFiles/artimage/2018/03/27/c_km601/cherrybl540.jpg',
     'ans_01': "다들 모여! 나들이 가자~",
     'ans_img02': 'https://mblogthumb-phinf.pstatic.net/MjAyMDA0MjlfOCAg/MDAxNTg4MTI3NzgxODQ0.m9VTkFJY7nWRJ63FzeFqek_ZeNQcXD116H19n0VsAyQg.x73v4TSymIwWYr84JzxXsP8YbQCcgB4eRRrMCb2xM34g.JPEG.designpress2016/%E3%85%87%E3%85%87.jpg?type=w800',
     'ans_02': "근손실 못참지!",
     'ans_img03': 'https://s3.ap-northeast-2.amazonaws.com/cloimage/home/rails/clo/public/ckeditor_assets/pictures/4044/content_.png.',
     'ans_03': "출출한데 뭐라도 사올까?",
     'ans_img04': 'data:image/jpeg;base64,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',
     'ans_04': "혼자 뒹굴뒹굴.."},

    {'idx': 4,
     'quiz': "서점에 들어간 당신,<br>가장 먼저 집어든 책의 제목은?",
     'ans_img01': 'https://search.pstatic.net/common/?src=http%3A%2F%2Fblogfiles.naver.net%2FMjAyMTA4MTZfMTM5%2FMDAxNjI5MTE5MjU2Mzcz.QcedJbdog5OGbbZS_zRnB4pVeBCw8_c29lnve3QdZGwg.yEoeHBal8GsZr172l3fYsrnh1gcm_rll1n35qVjH0Z4g.JPEG.tyutyu0918%2F20210816%25A3%25DF220332.jpg&type=sc960_832',
     'ans_01': "너와 함께라면 인생도 여행이다",
     'ans_img02': 'https://search.pstatic.net/common/?src=http%3A%2F%2Fblogfiles.naver.net%2FMjAyMDA1MDNfNjUg%2FMDAxNTg4NTA0OTk5MzIy.puGEUtUq11kG7xPk0Z9ONh3GFSFEM6Vf_TRPXoN9DCog.9O9B6-1d4N3xBivR8RjjJEH-oR8mbQkVxphiOxb9leAg.JPEG.alps_rabbit%2F%25C8%25FC%25BE%25F7%25B9%25EA%25B5%25E5_%25B7%25E7%25C7%25C1%25B9%25EA%25B5%25E5_%25C8%25A8%25C6%25AE_23.jpg&type=sc960_832',
     'ans_02': "백년운동",
     'ans_img03': 'https://search.pstatic.net/common/?src=http%3A%2F%2Fblogfiles.naver.net%2FMjAyMDA4MTJfNTkg%2FMDAxNTk3MTkzNDk5Nzgx.az9s03VzFF5F4oS7uQ1__JUNW03VmaKSBoQgXzTlfSYg.CRV0lyaIxR3_-_nKDXISbpLqJ5tctJWDpfO4X3ZFFxwg.JPEG.yuna080626%2FResized_20200722_195909.jpeg&type=sc960_832',
     'ans_03': "백종원의 집밥 요리 레시피",
     'ans_img04': 'https://t1.daumcdn.net/thumb/R720x0.fpng/?fname=http://t1.daumcdn.net/brunch/service/user/6MBC/image/dwuBe21QWH4HMFHeZkF7Pndj32w.png',
     'ans_04': "달러구트 꿈 백화점"},

    {'idx': 5,
     'quiz': "책을 구매하고 카페로 들어간<br>당신이 고른 메뉴는?",
     'ans_img01': 'https://blog.kakaocdn.net/dn/TV63N/btqKsnRKsA3/VeHC48yzG20wow2lYT5yc0/img.png',
     'ans_01': "역시 커피는 얼죽아!<br>아이스 아메리카노",
     'ans_img02': 'https://search.pstatic.net/common/?src=http%3A%2F%2Fblogfiles.naver.net%2FMjAxODA2MTVfMTQy%2FMDAxNTI5MDM0MzAwMjQ3.ubCTuvyg7LQBvBa8NBRibXReMw1PX3zz11qu8K9FjW4g.DLGoCzBKoDPJrsrNNT0EzdZuu4732naE3xH_pfujQNgg.JPEG.rendummy%2F%25B9%25CE%25C6%25AE%25C3%25CA%25C4%25DA1.JPG&type=sc960_832',
     'ans_02': "내 취향이 어때서!<br>민트초코라떼",
     'ans_img03': 'https://t1.daumcdn.net/cfile/blog/1337DB0B4A103FDD1D',
     'ans_03': "알콜은 나의 힘!<br>와인에이드",
     'ans_img04': 'https://masism.kr/wp-content/uploads/2018/01/t-1-1.jpg',
     'ans_04': "따뜻한게 제일이지!<br>핫초코"},

    {'idx': 6,
     'quiz': "음료를 다 마시고 카페를 나온 당신<br>오늘의 날씨는?",
     'ans_img01': 'https://search.pstatic.net/common/?src=http%3A%2F%2Fblogfiles.naver.net%2FMjAyMTA0MjNfNDYg%2FMDAxNjE5MTA2OTY4NDA2.CubHUvb21z_PAvLLrIok-JC_uHdASlGZqAbwF6qqDx8g.kjdbCHOboG5pi-OAL9y12phcu4Xcrbm2Jv88da-He8Ig.JPEG.lalille-201028%2Foutput_3681338891.jpg&type=sc960_832',
     'ans_01': "나들이 가고 싶다<br>맑은 날",
     'ans_img02': 'http://www.slist.kr/news/photo/201910/108298_205016_2046.jpg',
     'ans_02': "밖으로 나가면 안되는<br>폭염",
     'ans_img03': 'http://ojsfile.ohmynews.com/STD_IMG_FILE/2009/0610/IE001065706_STD.jpg',
     'ans_03': "파전에 막걸리가 땡기는<br>소나기",
     'ans_img04': 'https://newsimg.sedaily.com/2020/08/22/1Z6OFXPO5S_1.jpg',
     'ans_04': "간판 날아갈 거 같은<br>태풍"},
]

ansDoc = [
    {'idx': 1, 'type': 'A',
     'cover': 'https://blog.kakaocdn.net/dn/mSsTK/btreY4uZSGY/JG4YUDQ2LmLFdUlR4liXFK/img.png',
     'suggest': '“산책으로 바깥공기 만끽하기!”', },

    {'idx': 2, 'type': 'B',
     'cover': 'https://blog.kakaocdn.net/dn/csFn7r/btreZ15RV1F/FXSyNFkjUXXhGnPO1yO761/img.png',
     'suggest': '“근손실 방지! 홈트하자~”',
     'img-link1': 'https://i.ytimg.com/vi/myNjmnvI6x0/hqdefault.jpg',
     'title1': 'NO 층간소음 올인원 운동 - 40분 유산소운동 홈트 - 관절에 무리없이 체지방 태우기',
     'genre1': 'NO 층간소음 NO 스쿼트 - 40분 유산소운동 홈트 - 관절에 무리없이 체지방 태우기] - 땀 많이 나고 숨이 많이 차는 올인원 운동입니다. NO 층간소음 30동작 유산소 ...',
     'info1': '2021-01-22',
     'director1': '빅씨스',
     'link1': 'https://www.youtube.com/watch?v=myNjmnvI6x0',
     'img-link2': 'https://i.ytimg.com/vi/gMaB-fG4u4g/hqdefault.jpg',
     'title2': '전신 다이어트 최고의 운동 [칼소폭 찐 핵핵매운맛]',
     'genre2': '이번 영상은 정말! 정말! 맵습니다. 사실 운동 영상을 준비할 때 강도를 높이는 것은 그리 어려운 작업이 아닙니다. (스쿼트, 런지, 점핑잭, 버피등 반복..) 그래서 ...',
     'info2': '2021-05-24',
     'director2': 'Thankyou BUBU',
     'link2': 'https://www.youtube.com/watch?v=gMaB-fG4u4g',
     'img-link3': 'https://i.ytimg.com/vi/sqQpL1wKW6M/hqdefault.jpg',
     'title3': '12분 서서하는 복근운동 홈트레이닝 - 체지방 태우기는 보너스',
     'genre3': '서서하는 복근운동 홈트레이닝 - 복근운동을 제대로 하면서 체지방까지 태우는 루틴입니다. 서서하는 복근운동 은 누워서 할때보다 자극을 주기가 어렵기 때문에 루틴 ...',
     'info3': '2021-05-24',
     'director3': '빅씨스',
     'link3': 'https://www.youtube.com/watch?v=sqQpL1wKW6M'},

    {'idx': 3, 'type': 'C',
     'cover': 'https://blog.kakaocdn.net/dn/o2vyi/btre5PbYRGa/PE818HoBW7CUY55zOX2h3k/img.png',
     'suggest': '“맛있는건 언제나 옳다! 요리!”',
     'img-link1': 'https://i.ytimg.com/vi/tPf-KfZ6W84/hqdefault.jpg',
     'title1': '도톰한 감자튀김과 치즈소스 :: 바삭한 감자튀김 만들기 :: 감자요리 :: Fried Potatoes and cheese sauce :: French Fries',
     'genre1': '예상되는 질문들 하단에 TIP 으로 적어두었으니 참고하세요. 겉은 바삭 속은 촉촉한 감자튀김 만들었어요. 저처럼 두껍게 자르면 웨지감자 처럼 겉은 바삭, 속은 촉촉 ...',
     'info1': '2021-02-03',
     'director1': '매일맛나 delicious day',
     'link1': 'https://www.youtube.com/watch?v=tPf-KfZ6W84',
     'img-link2': 'https://i.ytimg.com/vi/LrTljxRQm4c/hqdefault.jpg',
     'title2': '요리먹방 :) 구독자 200만명 너무 감사합니다.🙏🏻 짜장 해물찜(랍스터테일, 전복, 주꾸미, 새우, 가리비, 오징어, 팽이버섯, 표고버섯, 새송이버섯) MUKBANG',
     'genre2': '여러분 덕분에 구독자가 200만명이 되었습니다. 너무 감사합니다. 기념으로 짜장소스 해물찜을 준비해봤어요~ 해물 : 랍스터테일, 전복, 주꾸미, 새우, 가리비, 오징어 ...',
     'info2': '2021-02-05',
     'director2': '보경 Bokyoung',
     'link2': 'https://www.youtube.com/watch?v=LrTljxRQm4c',
     'img-link3': 'https://i.ytimg.com/vi/ORQd1W9n4TA/hqdefault.jpg',
     'title3': '양배추를 이렇게 만들었더니 고기처럼 맛있어요! 순식간에 양배추 한 통이 사라져요 Cabbage Recipe',
     'genre3': '양배추를 이렇게 만들었더니 고기처럼 맛있어서 놀랐어요 요즘 무농약 양배추가 많이 보여서 자주 사먹다보니 새로운 양배추요리를 만들어 봤어요 집에 처치곤란한 ...',
     'info3': '2021-08-14',
     'director3': '하음쿠킹 Haeum Cooking',
     'link3': 'https://www.youtube.com/watch?v=ORQd1W9n4TA'
     },

    {'idx': 4, 'type': 'D',
     'cover': 'https://blog.kakaocdn.net/dn/dPqhNx/btre348O6qb/59pTuaAj4B0hJpeoLnOic0/img.png',
     'suggest': '“독서로 잔잔한 힐링하기!”',
     'img-link1': 'https://bookthumb-phinf.pstatic.net/cover/206/535/20653532.jpg?type=m1&udate=20210912',
     'title1': '오케팅', 'genre1': '특별하지 않아도 누구나 5% 부자가 되는 전략', 'info1': '대한출판사', 'director1': '오두환',
     'link1': 'https://book.naver.com/bookdb/book_detail.nhn?bid=20653532',
     'img-link2': 'https://bookthumb-phinf.pstatic.net/cover/196/181/19618143.jpg?type=m1&udate=20210912',
     'title2': '소크라테스 익스프레스', 'genre2': '철학이 우리 인생에 스며드는 순간', 'info2': '어크로스', 'director2': '에릭 와이너',
     'link2': 'https://book.naver.com/bookdb/book_detail.nhn?bid=19618143',
     'img-link3': 'https://bookthumb-phinf.pstatic.net/cover/207/771/20777131.jpg?type=m1&udate=20210912',
     'title3': '달러구트 꿈 백화점2', 'genre3': '단골손님을 찾습니다', 'info3': '팩토리나인', 'director3': '이미예',
     'link3': 'http://book.naver.com/bookdb/book_detail.nhn?bid=20777131'},

    {'idx': 5, 'type': 'F',
     'cover': 'https://blog.kakaocdn.net/dn/piJdH/btre5a1KXg3/Esxzje14oW7jg0bGtYfkD0/img.png',
     'suggest': '“오감만족! 넷플릭스 시청하기”',
     'img-link1':'https://images.justwatch.com/poster/246775914/s166',
     'title1':'알고있지만,',
     'genre1':'드라마, 로맨스',
     'info1':'시간 01:10분',
     'director1':'감독 : Kim Ga-ram',
     'link1':' https://www.netflix.com/kr/title/81435649',
     'img-link2':'https://images.justwatch.com/poster/116767348/s166',
     'title2':'킹덤',
     'genre2':'SF, 공포, 드라마, 스릴러, 액션',
     'info2':'',
     'director2':'출연자 : 주지훈, 류승룡, 배두나',
     'link2':' https://www.netflix.com/kr/title/80180171',
     'img-link3':'https://images.justwatch.com/poster/239555642/s166',
     'title3':'스위트홈',
     'genre3':'SF, 드라마',
     'info3':'',
     'director3':'감독 : Lee Eung-bok',
     'link3':' https://www.netflix.com/kr/title/81061734'}
]

likeDoc = [
    {'idx': 1, 'name':'like', 'count': 0},
]



db.qna.insert_many(doc);
db.ans.insert_many(ansDoc);
db.like.insert_many(likeDoc);