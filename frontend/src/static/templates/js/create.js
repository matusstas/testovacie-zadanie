$(document).ready(function() {
    // Hide error div when page is loaded
    var errorMessageUserId = document.getElementById('invalidUserIdMessage');
    errorMessageUserId.style.display = "none";

    $('form').on("submit", function(){
        var userId = parseInt(document.getElementById("formUserId").value);
        var title = document.getElementById("formTitle").value;
        var body = document.getElementById('formBody').value;

        var post = {
            "userId": userId,
            "title": title,
            "body": body,
        }

        $.ajax({
            type: 'POST',
            url: '/post',
            data: JSON.stringify(post),
            success: function(result) {
                if ('id' in result) {
                    var id = result['id'];
                    window.location.reload();
                    window.location.href = '/posts/' + id;   
                } else {
                    // Display error div with message
                    document.getElementById("invalidUserIdMessage").innerText = result['message'];
                    errorMessageUserId = document.getElementById('invalidUserIdMessage');
                    errorMessageUserId.style.display = "block";
                }
            }
        })
    });
});
