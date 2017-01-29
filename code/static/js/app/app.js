$(function() {
    $('#upload-file-btn').click(function() {
        var form_data = new FormData($('#file')[0]);
        $.ajax({
            type: 'POST',
            url: 'http://cfe81af2.ngrok.io/',
            data: form_data,
            contentType: false,
            cache: false,
            processData: false,
            async: false,
            success: function(data) {
                var last = window.location.href.substr(window.location.href.lastIndexOf('/') + 1);
                window.location.href = window.location.href.replace(last, "profile.html?w="+data.substring(2,7)+"&h="+data.substring(19,24));
            }
        });
    });
});