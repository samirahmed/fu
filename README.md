[CommandlineFu.com]: http://www.commandlinefu.com/commands/browse
[wiki]: https://github.com/samirahmed/fu/wiki/

# What is Fu?

A simple commandline utility for querying commandlinefu.com

## What is commandlinefu.com

[CommandlineFu.com] is an awesome website written by David Winterbottom
It has a collection of neat commandline one liners for the unix shell

## Why Fu ?

Fu makes commandlinefu more accessible because I find that I use
[CommandlineFu.com] most when actually in the commandline

## How do I use it?

It's easy to install, all you need to do is download and make

```
$ git clone git://github.com/samirahmed/fu.git
$ cd fu/
$ sudo make install
```

If that last step doesn't work you can use the setup.py

	$ sudo python setup.py install --record installRecords.txt

You can query fu by adding any search terms as arguments

For example if you want to search for how to "send binary mail attachment"

		$ fu send binary mail attachment                                           
		 1	#  Send email with one or more binary attachments
			echo "Body goes here" | mutt -s "A subject" -a /path/to/file.tar.gz recipient@example.com
			
		 2	#  Send a binary file as an attachment to an email
			uuencode archive.tar.gz archive.tar.gz | mail -s "Emailing: archive.tar.gz" user@example.com
			
			498ms total:2

### Dependencies and Fixes

It is possible you might not have some dependencies like argparse installed.

	$ sudo easy_install argparse
	
See the [wiki] for more help  

## Uninstalling

To remove fu you can do automagically with 

```
$ cd fu/
$ sudo make uninstall
```

Or you can do it manually by finding the files from your installRecords.txt file and removing them

One will be in your PYTHONPATH, the other in your /usr/local/ path probably

## Questions?

There is a wiki for more examples and info about usage.

Feel free to contribute if you have more ideas!




