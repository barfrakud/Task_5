# 5. Implement a CI/CD pipeline using Docker
## 1. Set up a Jenkins server in a Docker container.

### Run the Jenkins server
---
Run the jenkins docker image with the following command:
```
docker run -p 8080:8080 -p 50000:50000 -d -v jenkins_home:/var/jenkins_home jenkins/jenkins
```

List all running containers
```
docker ps
```

### Configure Jenkins server
---
#### Get logs from a specific container (image_id)
```
docker logs <image_id>
```

#### Copy initial password and paste to the web interface.
```
Jenkins initial setup is required. An admin user has been created and a password generated.
Please use the following password to proceed to installation:

e30ad9f35e1d44e894b20944fc389961

This may also be found at: /var/jenkins_home/secrets/initialAdminPassword
```

#### On web interface install suggested plugins.

#### Create first Admin User
```
Username: jenkins
Password: <Jenkins123>
Full Name: Jenkins
email: jenkins@email.com
```

#### Switch to english language
1. Install plugin Locale in Manage Jenkins
2. On Dashboard > Manage Jenkins > System > Locale > Default Language: set `en`

#### Install jenkins plugins
In plugin manager install plugins as follows:
```
Blue Ocean
Docker
Docker Pipeline
Docker Compose Build Step
```

## 2. Create a Jenkins pipeline that builds a Docker image when changes are pushed to a Git repository.

#### Prepare python application to be included in the image:
Create python app:
`app1.py` 

#### Prepare dockerfile to build an image:
Create dockerfile:
`Dockerfile`

### Verify the Dockerfile by building an image and running a container: 
```
docker build -t hello-bartek .
docker run -d -p 8888:5000 hello-bartek
```

## 3. Extend the pipeline to push the image to a private registry and deploy it to a Docker host.