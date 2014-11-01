#!/usr/bin/ruby
require 'cgi'
load 'functions.cgi'
$cgi = CGI.new
$params = $cgi.str_params

def input_action(action)
  case action
    when 'chat' then chat($user, $params['text'], $params['magic'])
  end
end


UserID = get_validated_id
if UserID != false
  print "Content-type: text/html\r\n\r\n"
else
  puts $cgi.header('Location'=>'index.cgi?msg=bad_pw')
  exit
end

$user = User.new(UserID)
input_action $params['action']

puts <<ENDTEXT
<html>
<head profile="http://www.w3.org/2005/10/profile">
<link rel="icon" 
      type="image/png" 
      href="images/favicon.ico">
<title>Chat</title>
<link rel=\"stylesheet\" type=\"text/css\" href=\"iceage.css\"/>

<body>
<a class="buttonlink" href="game.cgi">Return</a>
<hr>
#{html_chat_large(150)}
</body>
</html>
ENDTEXT
