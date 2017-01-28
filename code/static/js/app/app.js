uploadFile =function() {
    var file    = document.querySelector('input[type=file]').files[0];

    $.ajax({
        type: "POST",
        url: "http://cfe81af2.ngrok.io",

        files : file,
        processData: false,
        contentType: false,
        success: function (data) {
            console.log('yo');    }
    });
//d
}
