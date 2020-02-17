# Secure Code Advisor

tl;dr - **tailor made secure code guidelines for everyone**

Secure coding is always a challenge for orgs of any size. Everyone wants to shift left, but there is a serious lack of tools which can help with secure coding.

Secure code advisor aims to make this easy. Choose your product requirements and voila you get tailor-made and ready to use secure code guidelines.

Secure code advisor was born with this simple idea in mine - provide a open source repo which allows easy contribution for secure code principals, cheat sheets etc and make it easy to pick and choose the snippets according to your enterprise's requirements. 

## Run
This is app is built using pretty simple code on top of Flask (python) which reads the folder "kb" and produces a nice tree view of document for you to select. 

To run:
```
$ python3 app.py
```
Then navigate to http://127.0.0.1:5000/ and click on the lang, db, framework etc as per your req and push "Generate .md"

## Contribution
Fork this repo, refer to already existing structure and send me a PR for a new lang,framework,db etc. I will merge it for everyone.

## Thanks
Since this project is not about reinventing secure coding checklist, we will be heavily reusing many cheatsheets/checklist from the mother Internet
* https://github.com/OWASP/Go-SCP
* https://laravel.com/docs/4.2/security
* https://www.sqreen.com/checklists/php-security-checklist
* ..more..



