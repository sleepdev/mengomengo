function login()
{
  FB.login(function(response) {
    if (response.session)
      document.location = "/";
  });
}
function logout()
{
  FB.logout(function(response) {
    document.location = "/";
  })
}

/* sets up a facebook/twitter style get/post/del data feed */
function rest_feed(options)
{
  var rest_feed = this;
  var feed = options['feed'] || $('#feed');
  var feed_form = options['feed_form'] || $('#feed_form');
  var feed_submit = options['feed_submit'] || $('#feed_submit');
  var feed_more = options['feed_more'] || $('#feed_more');
  var url = options['url'];
  var template = options['template'] || '<li>{{text}}</li>';
  var start = 0;
  var limit = options['limit'] || 15;

  this.render( json ) {
    /* todo, fix to decide append or prepend */
    var html = template;
    for( k in json ){
      html = html.replace('{{'+k+'}}',json[k])
    }
    var dom = $(html);
    dom.data("rest_data",data);
    feed.append( dom );
    start = start + 1;
  }
  this.post = function( data ){
    var form_data = {}; 
    feed_form.children('[name]').each(function(i){
      form_data[i.attr('name')] = i.attr('value');
    });
    $.ajax({
      type: 'POST',
      dataType: 'json',
      url: url,
      data: form_data,
      success: function( data ){
        rest_feed.render(data);
      }
    });    
  }
  this.get = function() {
    $.ajax({
      type: 'GET', 
      dataType: 'json', 
      url: url, 
      data: {start: start, limit: limit},
      success: function( list ){
        $.each(list, rest_feed.render);
        if( list.length < limit ) feed_more.hide();
      }
    });
  }
  this.del = function( ui ){ 
    $.ajax({
        type: 'DELETE',
        url: rest_url,
        data: ui.data("rest_data")
    });
    ui.slideUp();
  }
  feed_submit.click(function(){ rest_feed.post(); });
  feed_more.click(function(){ rest_feed.get(); });
  this.get();
}

