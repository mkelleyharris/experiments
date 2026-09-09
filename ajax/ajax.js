// AJAX Hello World Demo http://www.hackorama.com/ajax

// Make a POST to the server 
// and pass on any data from browser
// via the XMLHTTPRequest

function talktoServer(){
	var req = newXMLHttpRequest();
	//register the callback handler function
  	var callbackHandler = getReadyStateHandler(req, updateMsgOnBrowser);
  	req.onreadystatechange = callbackHandler;
  	req.open("POST", "servertime.php", true);
  	req.setRequestHeader("Content-Type", "application/x-www-form-urlencoded");
  	//get the value from the text input element and send it to server
  	var testmsg = document.getElementById("testmsg");
  	var msg_value = testmsg.value;
  	req.send("msg="+msg_value);
}

function getFileContentsServer(){
	var req = newXMLHttpRequest();
	
	// Display some status, just for the sake of the demo. Not for real production.
	req.onreadystatechange=function()
	{
		switch(req.readyState)
		{
		case 1: 
			document.getElementById("msg2_display").innerHTML="Connection Established";	
			break;
		case 3: 
		    document.getElementById("msg2_display").innerHTML="Processing Request";	
			break;
		case 4: 
			if (req.status==200)
			{
	        	document.getElementById("msg2_display").innerHTML=req.responseText.split("\n").join("<br>");
	        }
	        break;
		default: 
			document.getElementById("msg2_display").innerHTML="Nothing";
		}	
	}
	
	//register the callback handler function	
  	//var callbackHandler = getReadyStateHandler(req, updateMsg2OnBrowser);
  	//req.onreadystatechange = callbackHandler;
  	//req.open("GET", "file1.txt", true);
  	req.open("GET", "getfilecontents.php", true);
  	req.setRequestHeader("Content-Type", "application/x-www-form-urlencoded");
  	req.send(null);
}


// This is the callback functions that gets called
// for the response from the server with the XML data

var lastPing = 0;
function updateMsgOnBrowser(testXML) {

	var test = testXML.getElementsByTagName("test")[0];
	var message = testXML.getElementsByTagName("message")[0];
	var ipClient = testXML.getElementsByTagName("ipClient")[0];
	var ipServer = testXML.getElementsByTagName("ipServer")[0];
	var nameServer = testXML.getElementsByTagName("nameServer")[0];

	var timestamp = test.getAttribute("timestamp");
	if (timestamp > lastPing) {
		lastPing = timestamp;

		var ipClient_value = ipClient.firstChild.nodeValue;
		var ipServer_value = ipServer.firstChild.nodeValue;
		var nameSever_value = nameServer.firstChild.nodeValue;
		var message_value = message.firstChild.nodeValue;

		var msg_display = document.getElementById("msg_display");
		msg_display.innerHTML = " Server got the  message: \"" + 
			message_value + "\"" +
			"<br>Client IP: "+ ipClient_value + "\"" +
			"<br>Server IP: "+ ipServer_value + "\"" +
			"<br>Server Host Name: "+ nameSever_value + "\"" +
			"<br>Server Timestamp: \""+ timestamp + "\"" ;
	}
}

function updateMsg2OnBrowser(testXML) {
    console.log('updateMsg2OnBrowser');
    console.log(testXML);

	var test = testXML.getElementsByTagName("test")[0];
	var contents = testXML.getElementsByTagName("contents")[0];

	//var timestamp = test.getAttribute("timestamp");
	if (http.readyState == 4) { //timestamp > lastPing) {
		lastPing = timestamp;

		var contents_value = contents.firstChild.nodeValue;

		var msg_display2 = document.getElementById("msg2_display");
		msg_display2.innerHTML = contents_value ;
	}
}

function newXMLHttpRequest() {
	var xmlreq = false;
	if (window.XMLHttpRequest) {
		xmlreq = new XMLHttpRequest();
	} 
	
   	return xmlreq;
} 

//register a listner callback function
function getReadyStateHandler(req, responseXmlHandler) {
	return function () {
	if (req.readyState == 4) {
		if (req.status == 200) {
        		responseXmlHandler(req.responseXML);
		} else {
			var hellomsg = document.getElementById("hellomsg");
			hellomsg.innerHTML = "ERROR: "+ req.status;
      		}
    	}
 	}
}

