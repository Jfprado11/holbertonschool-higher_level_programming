document.addEventListener("DOMContentLoaded", function () {
  $(function () {
    $("DIV#add_item").click(function () {
      const iteam = "<li>Item</li>";
      $("UL.my_list").append(iteam);
    });
    $("DIV#remove_item").click(function () {
      $("UL.my_list LI:last-child").remove();
    });
    $("DIV#clear_list").click(function () {
      $("UL.my_list LI").remove();
    });
  });
});
