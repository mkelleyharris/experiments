import re

str = u'dEV Coaches <devcoaches@external.cisco.com>,\
 playbook@external.cisco.com\
cc:	 Michael McNally <devcoaches@external.cisco.com>,\
 Chris LeBlanc <chleblan@cisco.com>,\
 Moreau Jerome <Moreau.Jerome@bcg.com>,\
 Harold Williams <Williams.Harold@bcg.com>,\
 Chuck Yannakopoulos <cyannako@cisco.com>,\
 Matt Hawkes <mhawkes@cisco.com>,\
 Bryce Billinger <brbillin@cisco.com>,\
 phharris@cisco.com\
'

str2 = """
<html><body>An anonymous person wrote:<blockquote>2nd entry writen....</blockquote>An anonymous person wrote:<blockquote>first entry</blockquote>
          <form action="/sign" method="post">
            <div><textarea name="content" rows="3" cols="60"></textarea></div>
            <div><input type="submit" value="Sign Guestbook"></div>
          </form>
        </body>
      </html>
"""

str3 = """<div><textarea name="content" rows="3" cols="60"></textarea></div>
"""

#results = re.findall(r'[\w.-]+@[\w.-]+', unicode(str,"utf-8"), flags=re.UNICODE)

#print str2

results = re.findall(r'<div>[\w\W]+\s?</div>', str2)
print results


