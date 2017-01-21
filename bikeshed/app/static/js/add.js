
// Image preview
function readURL(input) {

    if (input.files && input.files[0]) {
        var reader = new FileReader();

        reader.onload = function (e) {
            $('#preview_image').attr('src', e.target.result);
        }

        reader.readAsDataURL(input.files[0]);
    }
}

function registerUploadPreview(){
    $("#id_image").change(function(){
        readURL(this);
    });
}

// Form ajax handling

$('#add-form').ajaxForm(
{
    beforeSubmit: function(arr, $form, options) {
        $('#submit-id-submit').attr('disabled', 'true');
    },
    success: function(){
        // redirect to home
        window.location.replace("/");
    },
    error: function(err){
        if(err.status == 400){
            $("#form-content").html(err.responseText);
            registerUploadPreview();
        }else{
            alert('there was an error processing your request');
        }
    }
});

registerUploadPreview();