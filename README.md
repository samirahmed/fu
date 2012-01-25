[CommandlineFu.com] :http://www.commandlinefu.com/commands/browse
[ great guide on how to make Python script executable on unix ] http://effbot.org/pyfaq/how-do-i-make-a-python-script-executable-on-unix.htm

# What is cfu?

A simple commandline utility for querying commandlinefu.com

## What is commandlinefu.com

[CommandlineFu.com] is an awesome website written by David Winterbottom
It has a collection of neat commandline one liners for the unix shell

## Why cfu ?

cfu is makes commandlinefu more accessible because I find that I use
[CommandlineFu.com] most when actually in the commandline

## How do I use it?

You can query cfu by adding any search terms as arguments

For example if you want to search for how to "send binary mail attachment"

		$ python cfu.py send binary mail attachment
			
				# Send email with one or more binary attachments
					echo "Body goes here" | mutt -s "A subject" -a /path/to/file.tar.gz recipient@example.com
						
				# Send a binary file as an attachment to an email
					uuencode archive.tar.gz archive.tar.gz | mail -s "Emailing: archive.tar.gz" user@example.com
				
				804ms total:2

## Using as unix executable

There is a very easy way to make this script an executable and add it to path on unix

See this [great guide on how to make Python script executable on unix]

If you want to use cfu as a command you can 


