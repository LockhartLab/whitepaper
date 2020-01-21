
// how big should the sidenav get?
var sidenavSize = "100%";

// document ready functions
$(document).ready(function() {
  // initial check of window size
  checkSize();

  // if we resize, check again
  $(window).resize(checkSize);

  // add border and shadow on scroll
  $(document).scroll(function(){
    var scrollPercent = ($(window).scrollTop() / $('.container').outerHeight()) * 100;

    if (scrollPercent > 0) {
      $(".header").addClass("header-shadow");
    } else {
      $(".header").removeClass("header-shadow");
    }
  });

  // mouse clicks
  $(document).click(function(e) {
    var target = $(e.target);

    // deal with sidenav
    var isFlipped = $(".hamburger-bar1").hasClass("hamburger-bar1-flip");
    if (target.is(".hamburger, .hamburger-bar") && ! isFlipped) {
      turnSidenavOn();
    } else if (!target.is(".sidenav") && isFlipped) {
      turnSidenavOff();
    }

    // deal with previous from section controller
    if (target.is(".section-controller-previous")) {
      var previousSectionIndex = $(".section-controller-previous").index(target) - 1;
      if (previousSectionIndex >= 0) {
        var previousSection = $(".anchor").eq(previousSectionIndex);
        window.location.href = '#' + previousSection.attr('id');
      };
    };

    // deal with next from section controller
    if (target.is(".section-controller-next")) {
      var nextSectionIndex = $(".section-controller-next").index(target) + 1;
      if (nextSectionIndex < $(".anchor").length - 1) {
        var nextSection = $(".anchor").eq(nextSectionIndex);
        window.location.href = '#' + nextSection.attr('id');
      };
    };
  });

  // keypress
  $(document).on("keypress", function(e) {
    var key = e.which;

    // hamburger
    if (key === 109) {
      if ($(".hamburger-bar1").hasClass("hamburger-bar1-flip")) {
        turnSidenavOff();
      } else {
        turnSidenavOn();
      }
    };
  });
});

// check the window size
function checkSize() {
  if ($(".dummy").css("float") === "none") {
    sidenavSize = "100%";
  } else {
    sidenavSize = "15%";
  }
};

// turn sidenav on
function turnSidenavOn() {
  $(".hamburger-bar1").addClass("hamburger-bar1-flip");
  $(".hamburger-bar2").addClass("hamburger-bar2-flip");
  $(".hamburger-bar3").addClass("hamburger-bar3-flip");
  $(".sidenav").css("width", sidenavSize);
};

// turn sidenav off
function turnSidenavOff() {
  $(".hamburger-bar1").removeClass("hamburger-bar1-flip");
  $(".hamburger-bar2").removeClass("hamburger-bar2-flip");
  $(".hamburger-bar3").removeClass("hamburger-bar3-flip");
  $(".sidenav").css("width", "0px");
};
