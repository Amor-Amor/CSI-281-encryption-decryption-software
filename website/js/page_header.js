$(document).ready(function() {
    changeNavDimensions()
})

$(window).resize(function() {
    changeNavDimensions()
})

window.onload = function() {
    changeNavDimensions()
};

//Newer system: changes height of page-header to compensate for the page-header links going off of it
function changeNavDimensions() {
    
    var header = $("#page-header");
    var headerLinks = $(".header-links");

    //Adjusts where the header link buttons are centered
    center = headerLinks.width() / 2

    if(header.width() > 1600) {
        left = (header.width() / 2) - center
    }
    else if (header.width() > 1300) {
        left = (header.width() / 2) - center + 150
    }
    else if (header.width() > 900) {
        left = (header.width() / 2) - center + 200
    }
    else
    {
        left = "50px"
    }
    headerLinks.css("left", left);

    //Finds the max height of the header buttons
    var headBtns = $(".header-button a");  //Class headBtn, tag of a (link)
    var maxHeight = 0;
    headBtns.each(function(index) {
        if (maxHeight < $(this).height()) {
            maxHeight = $(this).height();
        }
    });

    //Adjusts the height of the header based on the height of the buttons
    if (maxHeight < 45){
        //When the screen is at a width where none of the buttons need to be resized
        header.css("height", "55px");
        headerLinks.css("height", "40px");  //Needs to edit the button height so the white background can obscure the logo
    }
    else {
        header.css("height", maxHeight + 16 + "px");
        headerLinks.css("height", maxHeight + 6 + "px");  //Needs to edit the button height so the white background can obscure the logo
    }
}