// $(document).ready(function() {
//     changeNavDimensions()
// })

// $(window).resize(function() {
//     changeNavDimensions()
// })

// window.onload = function() {
//     changeNavDimensions()
// };

// //Newer system: changes height of navbar to compensate for the navbar links going off of it
// function changeNavDimensions() {
    
//     var navbar = $("#navbar");
//     var navLinks = $(".nav-links");

//     //Adjusts where the Navbar link buttons are centered
//     center = navLinks.width() / 2

//     if(navbar.width() > 1600) {
//         left = (navbar.width() / 2) - center
//     }
//     else if (navbar.width() > 1300) {
//         left = (navbar.width() / 2) - center + 150
//     }
//     else if (navbar.width() > 900) {
//         left = (navbar.width() / 2) - center + 200
//     }
//     else
//     {
//         logo.css("height", "50px");
//         left = "50px"
//     }
//     navLinks.css("left", left);

//     //Finds the max height of the navbar buttons
//     var navBtns = $(".navBtn a");  //Class navBtn, tag of a (link)
//     var maxHeight = 0;
//     navBtns.each(function(index) {
//         if (maxHeight < $(this).height()) {
//             maxHeight = $(this).height();
//         }
//     });

//     //Adjusts the height of the navbar based on the height of the buttons
//     if (maxHeight < 45){
//         //When the screen is at a width where none of the buttons need to be resized
//         navbar.css("height", "55px");
//         navLinks.css("height", "40px");  //Needs to edit the button height so the white background can obscure the logo
//     }
//     else {
//         navbar.css("height", maxHeight + 16 + "px");
//         navLinks.css("height", maxHeight + 6 + "px");  //Needs to edit the button height so the white background can obscure the logo
//     }
// }