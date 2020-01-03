//
//@time : 2020/1/3上午10:45
//@Author: kongwiki
//@File: sign.py
//@Email: kongwiki@163.com
//

$(function () {
    $('.btn').click(function () {
        var $result = $('#result');
        var $username = $('input[name="username"]').val();
        var $password = $('input[name="password"]').val();
        $.ajax({
            url: '/signin',
            data: $('form').serialize(),
            // data: {'username': $username, 'password': $password},
            type: 'POST',
            dataType: 'json'
        }).done(function (data) {
            if (!data.r) {
                $result.html(data.rs);
            } else {
                $result.html(data.error);
            }
        });
    });
});