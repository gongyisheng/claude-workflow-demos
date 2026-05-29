echo 'export PATH="$HOME/.local/bin:$PATH"' >> ~/.bashrc

# install claude
curl -fsSL https://claude.ai/install.sh | bash
echo 'alias yolo="claude --dangerously-skip-permissions"' >> ~/.bashrc && source ~/.bashrc

# install uv
curl -LsSf https://astral.sh/uv/install.sh | sh

# install nodejs
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.40.4/install.sh | bash
\. "$HOME/.nvm/nvm.sh"
nvm install 24
node -v # Should print "v24.15.0".
npm -v # Should print "11.12.1".

# install ccusage
npm install -g ccusage