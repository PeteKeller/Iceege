#!/usr/bin/ruby
print "Content-type: text/html\r\n\r\n"
require 'cgi'
load 'mysql-connect.cgi'
load 'functions-mysql.rb'
mysql_connect
$cgi = CGI.new

def settlement_box
  settlements = mysql_select('settlements',{'allow_new_users'=>1})
  html = "\n\t<select name=\"settlement\" style=\"width:10em\">"
  html += "\n\t\t<option value=\"0\">None</option>"
  settlements.each_hash do
    |row|
    html += "\n\t\t<option value=\"#{row['id']}\""
    html += 'selected="yes" ' if $cgi['settlement'] == row['id']
    html += ">#{row['name']}, #{row['motto']}</option>"
  end
  html += "\n\t</select>"
end

Settlement_Box = settlement_box

puts <<ENDTEXT
<html>
<head profile="http://www.w3.org/2005/10/profile">
<link rel="icon" 
      type="image/png" 
      href="images/favicon.ico">
<title>Iceage - Home</title>
<link rel="stylesheet" type="text/css" href="iceage.css"/>
</head>
<body>
<div class='bigbox' style='height:600px'>
<table>
<tr>
<td>
<img alt='Cave painting logo' src='images/cave_artthumb.png' style='height:160px;display:inline' />
</td>

<td>
<h1>IceAge</h1>
<h2>Conquer. Explore. Settle. Trade. </h2>
<p><i>A free <a href='http://github.com/PeteKeller/Iceage'>open-source</a> browser-based massively multiplayer game</i></p>
</td>

<td>
<img alt='Cave painting logo' src='images/bw_hutsthumb.png' style='height:160px;display:inline' />
</td>


<td>
<a href="./screenshot.html"><img src='images/screenthumb.png'><br>[Screenshot]</a>
</td>

</tr>
</table>

<table>
<tr>

<td>

<div class='beigebox' style='width:15em'>

ENDTEXT
query = "SELECT COUNT(*) FROM `settlements`"
result = $mysql.query(query).fetch_hash
puts "<b>Settlements: #{result['COUNT(*)']}</b>"

puts "<br>"

query = "SELECT COUNT(*) FROM `grid`"
result = $mysql.query(query).fetch_hash
puts "<b>Map: #{result['COUNT(*)']} squares</b>"

puts <<ENDTEXT
</div>


<div class='beigebox' style='width:15em;margin-top:4px'>\n
<b>Sign in:</b><hr/>
ENDTEXT

case $cgi['msg']
  when "bad_pw"
    puts "\t<b>Incorrect username or password</b>\n"
  when "account_made"
    puts "\t<b>Player #{$cgi['username']} created! You may now log in:</b>\n"
end

puts <<ENDTEXT
<form method='POST' action='game.cgi'>
Username: <br>
<input type='text' class='text' name='username' maxLength='24'><br>
Password: <br>
<input type='password' class='text' name='password' length='32'>
<hr>
<input type='submit' style='margin-left:auto;margin-right:0px' value='Login'>
</form>

</div>

<div class='beigebox' style='width:15em;margin-top:4px'>\n
<!--<a class=\"buttonlink\" href=\"http://shin tolin.forumcircle.com\">Forum</a>
<a class=\"buttonlink\" href=\"http://shin tolin.wikia.com/wiki/Shin tolin\">Help/Wiki</a>-->
<a class=\"buttonlink\" href=\"faq.html\">FAQ</a>
<p>
<a class=\"buttonlink\" href=\"rankings.cgi\">Rankings</a>
<a class=\"buttonlink\" href=\"isaac.html\">Creator</a>
</div>

</td>

<td>
<div class='beigebox' style='width:30em'>
<i>People have wandered this world for millenia, hunting and gathering to survive during the ice age that is just ending. Some grow tired of the nomadic life, and are beginning to settle down. Forests make way for farmland, villages grow into towns and cities, and civilisations seek wealth, power, and glory.</i>

<hr>

<b>Hunt, or farm. Fight, or heal. Build, or conquer. Join of players in this free, browser-based world.</b>

<hr>

<div style='text-align:left;font-style:italic;'>
<ul>
<li>Work with other players to build a village, or try and survive the dangers of the wilderness</li>
<li>Find your fortune through farming, crafting, or trading</li>
<li>Explore a dynamic world, where every item, building and town is player-created</li>
<li>Shape the landscape, and write your own chapter in the history of Iceage</li>
</ul>
</div>
</td>

<td>

<div class='beigebox' style='width:15em'>\n
<b>Create a Character:</b>
<hr>
ENDTEXT

case $cgi['msg']
  when 'too_long'
    puts "\t<b>Username or password too long</b>\n"
  when 'too_short'
    puts "\t<b>Username or password too short</b>\n"
  when 'name_taken'
    puts "\t<b>Username is already taken</b>\n"
  when 'pw_not_match'
    puts "\t<b>Passwords do not match</b>\n"
  when 'invalid_name'
	puts "\t<b>Invalid username</b>\n"
  when 'no_email'
    puts "\t<b>Enter a valid email address</b>\n"
end

if $cgi['msg'] != 'account_made'
  puts <<ENDTEXT
    <form method='POST' action='signup.cgi'>
    Username: <br>
    <input type='text' class='text' name='username' maxLength='24'><br>
    E-mail: <br>
    <input type='text' class='text' name='email' length='100'><br>
    Password: <br>
    <input type='password' class='text' name='password_1' length='20'><br>
    Re-enter password: <br>
    <input type='password' class='text' name='password_2' length='20'><br>
    Settlement (optional, and can be changed later): <br>
    #{Settlement_Box}
    <hr>
    <input type='submit' value='Sign Up Now!' />
    </form>
ENDTEXT

else
  puts "\t<b>Player #{$cgi['username']} created! You may now log in.</b>\n"
end

puts <<ENDTEXT
</div>

</td>

</tr>
</table>
</div>
<font size = '-1' color='ff0000'>Server Time: #{Time.now}</font>
<br>
<div class='news'>
<h3>Updates</h3>

<h4>October 25th 2014</h4>
<ul>
<li>IT IS ALIVE. &lt;cue maniacal laughter&gt;</li>
</ul>

<h4>October 24th 2014</h4>
<ul>
<li>I installed Shintolin on this server and started customizing it.</li>
</ul>

</div>
</body>
</html>
ENDTEXT
