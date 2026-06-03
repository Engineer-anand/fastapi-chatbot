// ===== DOM ELEMENTS =====
const chatArea = document.getElementById('chat-area');
const chatInput = document.getElementById('chat-input');
const sendBtn = document.getElementById('send-btn');
const welcomeScreen = document.getElementById('welcome-screen');

// ===== STATE =====
let isGenerating = false;

// ===== INPUT HANDLING =====

// Auto-resize textarea
chatInput.addEventListener('input', () => {
    chatInput.style.height = 'auto';
    chatInput.style.height = Math.min(chatInput.scrollHeight, 120) + 'px';
    sendBtn.disabled = chatInput.value.trim() === '' || isGenerating;
});

// Enter to send, Shift+Enter for new line
chatInput.addEventListener('keydown', (e) => {
    if (e.key === 'Enter' && !e.shiftKey) {
        e.preventDefault();
        if (!sendBtn.disabled) sendMessage();
    }
});

sendBtn.addEventListener('click', sendMessage);

// ===== SUGGESTION CHIPS =====
function useSuggestion(chip) {
    chatInput.value = chip.textContent;
    chatInput.dispatchEvent(new Event('input'));
    sendMessage();
}

// ===== SEND MESSAGE =====
async function sendMessage() {
    const prompt = chatInput.value.trim();
    if (!prompt || isGenerating) return;

    // Hide welcome screen
    if (welcomeScreen) {
        welcomeScreen.style.display = 'none';
    }

    // Add user message to chat
    addMessage(prompt, 'user');

    // Clear input
    chatInput.value = '';
    chatInput.style.height = 'auto';
    sendBtn.disabled = true;
    isGenerating = true;

    // Add bot message placeholder with typing indicator
    const botMsgEl = addMessage('', 'bot', true);
    const contentEl = botMsgEl.querySelector('.msg-content');

    try {
        // ========================================
        // STREAMING API CALL (fetch + ReadableStream)
        // ========================================
        // Yeh browser se FastAPI ke /chat/stream endpoint ko POST request bhejta hai.
        // Response ek stream hota hai — matlab data chhote-chhote chunks mein aata hai,
        // poora response ek baar mein nahi aata.
        const response = await fetch('/chat/stream', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ prompt: prompt })
        });

        if (!response.ok) {
            throw new Error(`Server error: ${response.status}`);
        }

        // ReadableStream se chunks padhte hain
        const reader = response.body.getReader();
        const decoder = new TextDecoder();
        let fullText = '';

        // Remove typing indicator
        const typingEl = contentEl.querySelector('.typing-indicator');
        if (typingEl) typingEl.remove();

        while (true) {
            const { done, value } = await reader.read();
            if (done) break;

            // Chunk decode karke text mein convert karo
            const chunk = decoder.decode(value, { stream: true });
            fullText += chunk;
            contentEl.textContent = fullText;
            scrollToBottom();
        }

    } catch (error) {
        console.error('Chat error:', error);
        const typingEl = contentEl.querySelector('.typing-indicator');
        if (typingEl) typingEl.remove();
        contentEl.textContent = '⚠️ Something went wrong. Please try again.';
        contentEl.style.color = '#f87171';
    } finally {
        isGenerating = false;
        sendBtn.disabled = chatInput.value.trim() === '';
    }
}

// ===== ADD MESSAGE TO CHAT =====
function addMessage(text, role, showTyping = false) {
    const msgDiv = document.createElement('div');
    msgDiv.className = `message ${role}`;

    const avatar = document.createElement('div');
    avatar.className = 'msg-avatar';
    avatar.textContent = role === 'user' ? '👤' : '⚡';

    const content = document.createElement('div');
    content.className = 'msg-content';

    if (showTyping) {
        content.innerHTML = `
            <div class="typing-indicator">
                <span></span><span></span><span></span>
            </div>
        `;
    } else {
        content.textContent = text;
    }

    msgDiv.appendChild(avatar);
    msgDiv.appendChild(content);
    chatArea.appendChild(msgDiv);
    scrollToBottom();

    return msgDiv;
}

// ===== AUTO SCROLL =====
function scrollToBottom() {
    chatArea.scrollTo({
        top: chatArea.scrollHeight,
        behavior: 'smooth'
    });
}

// Focus input on load
chatInput.focus();
