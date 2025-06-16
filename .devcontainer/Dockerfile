FROM caltrans/pems:web

COPY . .

# install devcontainer requirements
RUN pip install -e .[dev,test]

# install docs requirements
RUN pip install --no-cache-dir -r docs/requirements.txt

# install streamlit requirements
RUN pip install --no-cache-dir -r streamlit_app/requirements.txt

# install AWS Copilot CLI (requires root permissions)
USER root
# download AWS Copilot CLI to /tmp to avoid write error (23) from curl command
WORKDIR /tmp

RUN curl -Lo copilot https://github.com/aws/copilot-cli/releases/latest/download/copilot-linux \
    && chmod +x copilot \
    && mv copilot /usr/local/bin/copilot

# Switch back to non-root user and app directory
USER $USER
WORKDIR /$USER/app
