# Variables
DOCKER_CMD = docker build

# Image definitions
IMAGE1 = flask-sensor-app
IMAGE2 = data-processing-service
IMAGE3 = dashboard-sensor-app
IMAGE4 = sensor-simulator

# Dockerfiles
DOCKERFILE1 = api-gateway\Dockerfile
DOCKERFILE2 = data_processing_service\Dockerfile
DOCKERFILE3 = dashboard\Dockerfile
DOCKERFILE4 = sensor-simulator\Dockerfile

# Build rules for each image
.PHONY: all $(IMAGE1) $(IMAGE2) $(IMAGE3) $(IMAGE4)

all: $(IMAGE1) $(IMAGE2) $(IMAGE3) $(IMAGE4)

$(IMAGE1):
	@echo "Building $(IMAGE1)"
	@$(DOCKER_CMD) -f $(DOCKERFILE1) -t $(IMAGE1) .

$(IMAGE2):
	@echo "Building $(IMAGE2)"
	@$(DOCKER_CMD) -f $(DOCKERFILE2) -t $(IMAGE2) .

$(IMAGE3):
	@echo "Building $(IMAGE3)"
	@$(DOCKER_CMD) -f $(DOCKERFILE3) -t $(IMAGE3) .

$(IMAGE4):
	@echo "Building $(IMAGE4)"
	@$(DOCKER_CMD) -f $(DOCKERFILE4) -t $(IMAGE4) .


# To build images in parallel, use 'make -j N' where N is the number of parallel jobs
