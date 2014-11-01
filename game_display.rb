puts <<ENDTEXT
<html>

<head profile="http://www.w3.org/2005/10/profile">
<link rel="icon" 
      type="image/png" 
      href="images/favicon.ico">
<title>Iceage - Conquer. Explore. Settle. Trade.</title>
<link rel="stylesheet" type="text/css" href="iceage.css" />
</head>
<body>
<div class="bigbox">

<div class="map">
#{Location_Bar}
#{Map}
</div>

<div class="gamebox statsbox">
#{Player_Data}
</div>

<div class="gamebox buttonsbox">
  <a class="buttonlink" href="skills.cgi">Skills</a>
  <a class="buttonlink" href="map.cgi">Map</a>
  <a class="buttonlink" href="contacts.cgi">Contacts</a>
  <a class="buttonlink" href="rankings.cgi">Rankings</a>
<!--  <a class="buttonlink" href="http://shin tolin.forumcircle.com">Forum</a>
  <a class="buttonlink" href="http://shin tolin.wikia.com/wiki/Shin tolin">Help/Wiki</a> -->
  <a class="buttonlink" href="faq.html">FAQ</a>
  #{Logout_Button}

</div>

<table class="infotable">
  <tr>
    <td colspan="2">
      <div style="opacity:.82" class="gamebox actionbox">
  #{Action_Forms}
      </div>
    </td>
  </tr>
  <tr>
    <td colspan="2">
      <div style="opacity:.82" class="gamebox infobox">
        <div style="beigeoverlay">
ENDTEXT

puts '<b><i>' + Dazed_Message + "</i></b>\n<br>\n" if Dazed_Message != ''
puts '<b>' + Action_Outcome + "</b>\n" if Action_Outcome != ''
puts ' <b>' + Tired_Message + "</b>\n" if Tired_Message != ''
puts "<br>\n<br>\n" if Action_Outcome != '' || Tired_Message != ''
puts Location_Info

puts <<ENDTEXT
        </div>
      </div>
    </td>
  </tr>
  <tr>
    <td>
      <div style="opacity:.82" class="gamebox invbox">
        <b>Weight: #{Encumberance}</b>
	<hr>
        <i>You are carrying:</i>
	#{Inventory}
        <hr>
        #{Drop}
      </div>
    </td>
    <td>
ENDTEXT

if Messages != ''
  puts "<div class=\"gamebox msgbox\">#{Messages}</div>"
end

puts <<ENDTEXT
      <div class="gamebox">
       <b>Chat:</b>
        <div class="chatbox">
        #{html_chat_box(30)}
        <center><br>
         <a class="buttonlink" href="chat.cgi">Chat page</a>
        </center><br>
      </div> 
       #{html_action_form('Chat',false,nil,'game.cgi') {
    html_text_box(200)}}
     </div>
    </td>
  </tr>
</table>
</div>
</body>
</html>
ENDTEXT
