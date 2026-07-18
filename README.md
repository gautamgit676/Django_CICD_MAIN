This complate deployment project 

= Dockerfile (image create )

= DOCKER.COMPOSE.YML (multiple container hendal)
    = redis
    = celeary
    = db
    = nginx

= CICD (github actions) (push code automatic in aws ec2)
    = code push diract in aws ec2 


note : two method code push direct on aws 

1 :git clone in ec2  and now only we need push code from terminal 
    : all configers in github/workflow/deploy.yml

2 ; all thigs copy in github/workflow/deploy.yml cpy nginx and yml file no need colne in ec2

note : .env all time we need manuly upload in ec2