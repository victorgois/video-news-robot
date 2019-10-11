var items = $('.nameList').find('li').map(function() {
    var item = { };
  
    item.id = this.value;
    item.title = $(this).text();
  
    return item;
  });