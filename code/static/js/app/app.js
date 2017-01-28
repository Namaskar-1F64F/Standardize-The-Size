uploadFile =function() {
    var file    = document.querySelector('input[type=file]').files[0];

    $.ajax({
        type: "POST",
        url: "http://344fae2a.ngrok.io/uploads/"+file.name,
        data: file,
        processData: false,
        contentType: false,
        success: function (data) {
            console.log('yo');    }
    });

}