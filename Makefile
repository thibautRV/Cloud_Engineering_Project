# Variables
DOCKER_CMD = docker build
DOCKER_USER = papyrgb

# Image definitions
IMAGE1 = flask-sensor-app
IMAGE2 = data-processing-service
IMAGE3 = dashboard-sensor-app

# Dockerfiles
DOCKERFILE1 = https://raw.githubusercontent.com/thibautRV/Cloud_Engineering_Project/main/api-gateway/Dockerfile
DOCKERFILE2 = https://raw.githubusercontent.com/thibautRV/Cloud_Engineering_Project/main/data_processing_service/Dockerfile
DOCKERFILE3 = https://raw.githubusercontent.com/thibautRV/Cloud_Engineering_Project/main/dashboard/Dockerfile

# Build rules for each image
.PHONY: all $(IMAGE1) $(IMAGE2) $(IMAGE3)

all: $(IMAGE1) $(IMAGE2) $(IMAGE3)

$(IMAGE1):
	@echo "Building $(IMAGE1)"
	@$(DOCKER_CMD) -f $(DOCKERFILE1) -t $(IMAGE1) .
	@docker tag $(IMAGE1) $(DOCKER_USER)/$(IMAGE1):latest
	@docker push $(DOCKER_USER)/$(IMAGE1):latest

$(IMAGE2):
	@echo "Building $(IMAGE2)"
	@$(DOCKER_CMD) -f $(DOCKERFILE2) -t $(IMAGE2) .
	@docker tag $(IMAGE2) $(DOCKER_USER)/$(IMAGE2):latest
	@docker push $(DOCKER_USER)/$(IMAGE2):latest

$(IMAGE3):
	@echo "Building $(IMAGE3)"
	@$(DOCKER_CMD) -f $(DOCKERFILE3) -t $(IMAGE3) .
	@docker tag $(IMAGE3) $(DOCKER_USER)/$(IMAGE3):latest
	@docker push $(DOCKER_USER)/$(IMAGE3):latest

# To build images in parallel, use 'make -j N' where N is the number of parallel jobs
