$(".card").on('click', function(){
    var href = $(this).attr('data-href');
    window.location.replace(href);
})

function reloadList(){
    var url = $("#sort-selector").val();

    $(".bikes-content").addClass('hide');
    $(".loading-content").removeClass('hide');

    $(".bikes-content").html('');
    $.get(url, { },
      function(data){

        for(dataIndex in data){
            var bike = data[dataIndex];

            var template = $('#bike_template').html();
            template = template.replace('__url__', '/show/'+bike.id)
            template = template.replace('__image__', bike.image.thumbnail)
            template = template.replace('__bike_model__', bike.model)
            template = template.replace('__bike_price__', bike.price)

            $(".bikes-content").append(template);
        }

        $(".card").on('click', function(){
            var url = $(this).attr('data-href')

            window.location.replace(url);
        });

        $('.loading-content').addClass('hide');
        $(".bikes-content").fadeIn();
        $(".bikes-content").removeClass('hide');

    });
}

$("#sort-selector").on('change', reloadList);
