// AI聊天组件
class AIChatComponent {
    constructor() {
        this.isOpen = false;
        // 现在应该通过Flask后端获取API密钥，而不是在前端硬编码
        this.apiURL = '/api/ai-chat'; // 使用后端代理API
        this.model = 'deepseek-chat';
        
        this.initializeComponent();
    }

    initializeComponent() {
        this.createFloatingButton();
        this.createChatWindow();
        this.setupEventListeners();
        this.loadSystemPrompt();
    }

    createFloatingButton() {
        const floatingBtn = document.createElement('div');
        floatingBtn.id = 'ai-chat-float';
        floatingBtn.innerHTML = `
            <div id="ai-chat-button" class="ai-chat-button">
                <i class="fas fa-robot"></i>
            </div>
        `;
        document.body.appendChild(floatingBtn);
    }

    createChatWindow() {
        const chatWindow = document.createElement('div');
        chatWindow.id = 'ai-chat-window';
        chatWindow.className = 'ai-chat-window hidden';
        chatWindow.innerHTML = `
            <div class="ai-chat-header">
                <h3>AI 智能助手</h3>
                <button id="ai-close-btn" class="ai-close-btn">&times;</button>
            </div>
            <div class="ai-chat-body">
                <div class="ai-settings">
                    <label for="ai-system-prompt">系统提示词:</label>
                    <textarea id="ai-system-prompt" rows="2" placeholder="设置AI助手的行为方式...">你是全球高中数据洞察仪表盘的专属数据分析师。你的职责是帮助用户理解和分析页面中展示的数据内容。

你只能回答以下与页面数据相关的问题：
1. 学校数据统计：学校数量、分布、排名
2. 国家分布数据：各国学校数量占比、地域分布
3. 学费统计数据：预算信息、费用变化趋势
4. 时间线数据：学校成立时间、存在时间统计
5. 学科统计数据：学科开设情况、学科分布
6. 图表数据解读：饼图、柱状图、折线图、气泡图中的具体数据含义

对于所有与页面数据无关的问题，包括但不限于：
- 技术实现细节
- 代码相关问题
- 项目结构
- 编程技术
- 通用知识问答
- 其他领域咨询

你必须回答："抱歉，我只能回答与全球高中数据洞察仪表盘中数据内容相关的问题。您的问题涉及其他方面，我无法回答。"

请基于页面显示的数据内容提供专业、准确的数据分析和解读。当用户询问与数据相关的问题时，提供详细的数据分析。当问题与数据无关时，礼貌地拒绝回答并说明限制。</textarea>
                </div>
                <div id="ai-messages" class="ai-messages">
                    <div class="ai-message ai-assistant-message">
                        <strong>AI助手:</strong> 您好！我是全球高中数据洞察仪表盘的专属数据分析师，专门为您解读页面中的数据内容。您可以问我关于学校数据、国家分布、学费统计、时间线等数据相关的问题。
                    </div>
                </div>
                <div class="ai-input-area">
                    <div class="ai-text-input">
                        <input type="text" id="ai-question" placeholder="请输入您的问题..." autocomplete="off">
                        <button type="button" id="ai-send-btn">发送</button>
                    </div>
                </div>
            </div>
        `;
        document.body.appendChild(chatWindow);
    }

    setupEventListeners() {
        // 浮动按钮点击事件
        document.getElementById('ai-chat-button').addEventListener('click', () => {
            this.toggleChatWindow();
        });

        // 关闭按钮点击事件
        document.getElementById('ai-close-btn').addEventListener('click', () => {
            this.closeChatWindow();
        });

        // 发送消息事件
        document.getElementById('ai-send-btn').addEventListener('click', () => {
            this.sendMessage();
        });

        // 按Enter键发送消息
        document.getElementById('ai-question').addEventListener('keypress', (e) => {
            if (e.key === 'Enter') {
                this.sendMessage();
            }
        });
        
        // 监听system prompt变化，保存到本地存储
        document.getElementById('ai-system-prompt').addEventListener('input', () => {
            this.saveSystemPrompt();
        });
    }

    loadSystemPrompt() {
        const savedPrompt = localStorage.getItem('ai-system-prompt');
        if (savedPrompt) {
            document.getElementById('ai-system-prompt').value = savedPrompt;
        }
    }

    saveSystemPrompt() {
        const prompt = document.getElementById('ai-system-prompt').value;
        localStorage.setItem('ai-system-prompt', prompt);
    }

    toggleChatWindow() {
        const chatWindow = document.getElementById('ai-chat-window');
        if (this.isOpen) {
            this.closeChatWindow();
        } else {
            chatWindow.classList.remove('hidden');
            this.isOpen = true;
            // 将焦点设置到输入框
            document.getElementById('ai-question').focus();
        }
    }

    closeChatWindow() {
        const chatWindow = document.getElementById('ai-chat-window');
        chatWindow.classList.add('hidden');
        this.isOpen = false;
    }



    async sendMessage() {
        const questionInput = document.getElementById('ai-question');
        const systemPromptInput = document.getElementById('ai-system-prompt');
        const question = questionInput.value.trim();
        const systemPrompt = systemPromptInput.value.trim() || '你是一个有用的AI助手，能够回答问题并提供帮助。';

        if (!question) {
            alert('请输入问题！');
            return;
        }

        // 添加用户消息到对话
        this.addMessage('user', question);
        
        // 清空输入框
        questionInput.value = '';

        try {
            // 显示加载状态
            const loadingMsg = this.addMessage('assistant', 'AI正在思考中...');
            
            // 调用后端API（后端将处理API密钥和与DeepSeek的通信）
            const response = await fetch(this.apiURL, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({
                    message: question,
                    system_prompt: systemPrompt
                })
            });

            if (!response.ok) {
                throw new Error(`API请求失败: ${response.statusText}`);
            }

            const result = await response.json();
            const aiResponse = result.response || '没有收到AI的回应。';

            // 更新AI消息内容
            loadingMsg.innerHTML = `<strong>AI助手:</strong> ${this.formatMessage(aiResponse)}`;
        } catch (error) {
            // 更新AI消息内容为错误信息
            const errorMsg = document.querySelector('#ai-messages .ai-message:last-child');
            if (errorMsg) {
                errorMsg.innerHTML = `<strong>AI助手:</strong> <span style="color: #ff6b6b;">错误: ${error.message}</span>`;
            }
            console.error('AI请求错误:', error);
        }
    }

    addMessage(role, content) {
        const messagesContainer = document.getElementById('ai-messages');
        const messageDiv = document.createElement('div');
        messageDiv.className = `ai-message ai-${role}-message`;
        
        if (role === 'user') {
            messageDiv.innerHTML = `<strong>您:</strong> ${this.formatMessage(content)}`;
        } else {
            messageDiv.innerHTML = `<strong>AI助手:</strong> ${this.formatMessage(content)}`;
        }
        
        messagesContainer.appendChild(messageDiv);
        
        // 滚动到底部
        messagesContainer.scrollTop = messagesContainer.scrollHeight;
        
        return messageDiv;
    }

    formatMessage(content) {
        // 简单的消息格式化，将换行符转换为<br>
        return content.replace(/\n/g, '<br>');
    }
}

// 初始化AI聊天组件
document.addEventListener('DOMContentLoaded', function() {
    new AIChatComponent();
});