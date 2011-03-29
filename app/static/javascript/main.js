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
  if ( !(this instanceof rest_feed) )
      return new rest_feed(options);

  var url = options['url'];
  var feed_api = this;
  var feed = options['feed'] || $('#feed');
  var template = options['template'] || '<li>{{text}}</li>';
  var start = 0;
  var limit = options['limit'] || 15;

  this.render = function( json ) {
    /* todo, fix to decide append or prepend order */
    var html = template;
    for( var k in json ){
      html = html.replace('{{'+k+'}}',json[k]);
      alert( k );
    }
    var dom = $(html);
    dom.data("rest_data",json);
    feed.find('.list').append( dom );
    start = start + 1;
  }
  this.post = function( data ){
    var form_data = {}; 
    feed.find('.form [name]').each(function(i){
      form_data[i.attr('name')] = i.attr('value');
    });
    $.ajax({
      type: 'POST',
      dataType: 'json',
      url: url,
      data: feed.find('.feedform'),
      success: function( data ){
        feed_api.render(data);
      }
    });    
  }
  this.get = function() {
    $.ajax({
      type: 'GET', 
      dataType: 'json', 
      url: url, 
      data: {start: start, limit: limit},
      success: function( json ){
        $.each(json.data, feed_api.render);
        if( json.data.length < limit ) feed.find('.more').hide();
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
  feed.find('.submit').click(function(){ feed_api.post(); });
  feed.find('.more').click(function(){ feed_api.get(); });
  this.get();
}

