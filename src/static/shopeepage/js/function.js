const monthNames = ["Jan", "Feb", "Mar", "Apr", "May", "June", "July", "August", "September", "Oct", "Nov", "Dec"];
$("#commentform").submit(function (e) {
    e.preventDefault(); // Ngăn chặn hành vi mặc định của form
    console.log("hello world!");
    let dt = new Date()
    let time = dt.getDay() + " " + monthNames[dt.getUTCMonth()] + ", " + dt.getFullYear()
    $.ajax({
        data: $(this).serialize(),
        method: $(this).attr("method"),
        url: $(this).attr("action"),
        dataType: "json",
        success: function (response) {
            console.log("comment successfully", response);
            if (response.bool == true) { // Sửa thành ===
                $("#review-res").html("Review added successfully");
                $(".hide-comment-form").hide(); // Sửa thành .hide-comment-form
                $(".add-review").hide(); // Sửa thành .add-review
                // Thêm đánh giá vào danh sách đánh giá
                let _html = '<div class="single-comment justify-content-between d-flex mb-30">'
                _html += '<div class="user justify-content-between d-flex">'
                _html += '<div class="thumb text-center" style="margin-right: 20px;">'
                _html += '<img src="http://127.0.0.1:8000/static/shopeepage/img/df-user.png"style="max-width:25px" ;>'
                _html += '<span href="#" class="text-brand">' + response.context.user + '</span>'
                _html += '</div>'
                _html += '<div class="dec">'
                _html += '<div class="d-flex justify-content-between mb-10">'
                _html += '<div class="d-flex align-items-center">'
                _html += '<span class="" style="margin-right: 20px;">' + time + '</span>'
                _html += '</div>'

                for (let i = 0; i < response.context.rating; i++) {
                    _html += ' <i class="fa fa-star "  aria-hidden="true"></i>'
                }

                _html += '</div>'
                _html += '<p class="mb-10"> ' + response.context.review + '</p>'
                _html += '</div>'
                _html += '</div>'
                _html += '</div>'
                $(".comment-list").prepend(_html);
            }
        }
    });
});



// 
$(document).ready(function () {
    $(".filter-checkbox").on("click", function (e) {
        let filter_object = {}
        $(".filter-checkbox:checked").each(function () {
            let filter_value = $(this).val()
            let filter_key = $(this).data("filter")
            filter_object[filter_key] = filter_object[filter_key] || [];
            filter_object[filter_key].push(filter_value);
        });

        // Gửi dữ liệu AJAX nếu có ít nhất một checkbox đã được chọn
        if (Object.keys(filter_object).length > 0) {
            $.ajax({
                url: '/filter-product',
                data: filter_object,
                dataType: 'json',
                beforeSend: function () {
                    console.log("Sending data");
                },
                success: function (res) {
                    console.log("Success: " + res);
                    $("#filter-product").html(res.data);
                },
                error: function (error) {
                    console.error("Error: " + error.statusText);
                }
            });
        }
        $("#max")
    });
});


// add to cart
$("#add-to-cart-btn").on("click", function(){
    let quantity = $("#product-quatity").val()
    let product_title = $(".product-title").val()
    let product_id = $(".product-id").val()
    let product_price = $("#current-product-price").text()
    let this_val = $(this)
    console.log("quality", quantity)
    console.log("product_title", product_title)
    console.log("product_id", product_id)
    console.log("curee", product_price)
    console.log("val", this_val)

    $.ajax({
        url: '/add-to-cart',
        dataType: 'json',
        data: {
            'id': product_id,
            'qty': quantity,
            'title': product_title,
            'price': product_price,
        },
        beforeSend: function(){
            console.log(" add product")
        },
        success: function( response ){
            this_val.html("Item add cart")
            console.log("success final")
        }
    })
})