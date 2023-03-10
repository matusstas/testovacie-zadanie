$(document).ready(function() {
    // When page is loaded then replace \n with \r\n -> new line
    var body = document.getElementById('formBody').value;
    body = body.replace(/\\n/g, '\r\n');
    document.getElementById("formBody").value = body;

    https://getbootstrap.com/docs/5.0/forms/validation/?
    $('form').on("submit", function(){
        var id = parseInt(document.getElementById("formId").value);
        var userId = parseInt(document.getElementById("formUserId").value);
        var title = document.getElementById("formTitle").value;
        var body = document.getElementById('formBody').value;

        var post = {
            "id": id,
            "userId": userId,
            "title": title,
            "body": body,
        }

        $.ajax({
            type: 'PUT',
            url: '/posts/' + id,
            data: JSON.stringify(post),
        })
    });
});


function deletePost(id) {
    fetch('/posts/' + id, {
        method: 'DELETE',
    }).then(function(){
        window.location.reload();
        window.location.href = '/posts';
    });
}
