function login()
{
  if( typeof FB == 'undefined' )
    document.location = "/login";
  else
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

function play(options)
{
  var service = options['service'] || 'youtube';
  var video_id = options['video_id'];
  if( service == 'youtube' )
  {
    var template = '<object width="425" height="344">'+
      '<param name="movie" value="http://www.youtube.com/v/{video_id}?fs=1"</param>'+
      '<param name="allowFullScreen" value="true"></param>'+
      '<param name="allowScriptAccess" value="always"></param>'+
      '<embed src="http://www.youtube.com/v/{video_id}?fs=1" '+
        'type="application/x-shockwave-flash" '+
        'allowfullscreen="true" '+
        'allowscriptaccess="always" '+
        'width="425" height="344">'+
      '</embed>'+
    '</object>';
    template = template.replace('{video_id}',video_id);
    $('#player').html( template );
  } else {
    alert('unrecognized video-hosting service: '+service);
  }
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
        $.each( json.data, function(i,v){feed_api.render(v)} );
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

function fb_login() {
  /* look at fb javascript sdk... */
  var h = 400; var w = 580;
  var left = (screen.width/2)-(w/2);
  var top = (screen.height/2)-(h/2);
  var newwindow = window.open('http://mengomengo.com/facebook_auth',null,'height='+h+',width='+w+', toolbar=0, resizable=0, scrollbars=0, location=0, menubar=0, top='+top+', left='+left);
  if (window.focus) {newwindow.focus()}
}

$('.toggle').click( function(){ this.toggle() } );
