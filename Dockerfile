FROM quay.io/operator-framework/ansible-operator:v1.22.2

# Added by RR
# COPY additional-pip-requirements.txt ${HOME}/requirements.txt
# RUN pip3 install -r ${HOME}/requirements.txt

COPY requirements.yml ${HOME}/requirements.yml
RUN ansible-galaxy collection install -r ${HOME}/requirements.yml \
 && chmod -R ug+rwx ${HOME}/.ansible

COPY watches.yaml ${HOME}/watches.yaml
COPY roles/ ${HOME}/roles/
COPY playbooks/ ${HOME}/playbooks/
