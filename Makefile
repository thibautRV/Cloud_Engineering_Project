# Variables
DOCKER_USER = papyrgb

# Image definitions
IMAGE1 = flask-sensor-app
IMAGE2 = data-processing-service
IMAGE3 = dashboard-sensor-app
IMAGE4 = postgres-db

# Dockerfiles
DOCKERFILE1 = https://raw.githubusercontent.com/thibautRV/Cloud_Engineering_Project/main/api-gateway/Dockerfile
DOCKERFILE2 = https://raw.githubusercontent.com/thibautRV/Cloud_Engineering_Project/main/data_processing_service/Dockerfile
DOCKERFILE3 = https://raw.githubusercontent.com/thibautRV/Cloud_Engineering_Project/main/dashboard/Dockerfile
DOCKERFILE4 = https://raw.githubusercontent.com/thibautRV/Cloud_Engineering_Project/main/database/Dockerfile

# Build rules for each image
.PHONY: all $(IMAGE1) $(IMAGE2) $(IMAGE3) $(IMAGE4)

all: $(IMAGE1) $(IMAGE2) $(IMAGE3) $(IMAGE4)

$(IMAGE1):
	@echo "Building $(IMAGE1)"
	@docker build -f $(DOCKERFILE1) -t $(IMAGE1) .
	@docker tag $(IMAGE1) $(DOCKER_USER)/$(IMAGE1):latest
	@docker push $(DOCKER_USER)/$(IMAGE1):latest

$(IMAGE2):
	@echo "Building $(IMAGE2)"
	@docker build -f $(DOCKERFILE2) -t $(IMAGE2) .
	@docker tag $(IMAGE2) $(DOCKER_USER)/$(IMAGE2):latest
	@docker push $(DOCKER_USER)/$(IMAGE2):latest

$(IMAGE3):
	@echo "Building $(IMAGE3)"
	@docker build -f $(DOCKERFILE3) -t $(IMAGE3) .
	@docker tag $(IMAGE3) $(DOCKER_USER)/$(IMAGE3):latest
	@docker push $(DOCKER_USER)/$(IMAGE3):latest

$(IMAGE4):
	@echo "Building $(IMAGE4)"
	@docker build -f $(DOCKERFILE4) -t $(IMAGE4) .
	@docker tag $(IMAGE4) $(DOCKER_USER)/$(IMAGE4):latest
	@docker push $(DOCKER_USER)/$(IMAGE4):latest

# To build images in parallel, use 'make -j N' where N is the number of parallel jobs
