set -e
cp -f /tmp/host.gitconfig /root/.gitconfig
chmod 600 /root/.gitconfig

git config --global --add safe.directory "${WORKSPACE_FOLDER}"
git config --global user.name \"$GIT_USER_NAME\" 
git config --global user.email \"$GIT_USER_EMAIL\"

cd "${WORKSPACE_FOLDER}"
uv lock --upgrade
uv sync --refresh