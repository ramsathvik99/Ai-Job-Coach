document.addEventListener('DOMContentLoaded', () => {
  setTimeout(() => {
    const messages = document.querySelectorAll('.flash-message');
    messages.forEach(msg => {
      msg.style.opacity = '0';
      msg.style.transform = 'translateY(-10px)';
      setTimeout(() => msg.remove(), 500);
    });
  }, 3000);

  const nameInput = document.getElementById('nameInput');
  const nameError = document.getElementById('nameError');

  if (nameInput) {
    nameInput.addEventListener('input', () => {
      const namePattern = /^[A-Za-z\s]*$/;
      if (!namePattern.test(nameInput.value)) {
        nameError.style.display = 'block';
      } else {
        nameError.style.display = 'none';
      }
    });
  }

  // === LOGIN SCRIPT ===
  const loginForm = document.querySelector('#login-form');
  if (loginForm) {
    const email = loginForm.querySelector('input[name="email"]');
    const password = loginForm.querySelector('input[name="password"]');
    const toggleBtn = loginForm.querySelector('.toggle-password');

    toggleBtn?.addEventListener('click', () => {
      password.type = password.type === 'password' ? 'text' : 'password';
      toggleBtn.textContent = password.type === 'password' ? 'Show' : 'Hide';
    });

    loginForm.addEventListener('submit', (e) => {
      if (!email.value || !password.value) {
        e.preventDefault();
        alert('Please fill in both email and password.');
        return;
      }

      const emailPattern = /^[^ ]+@[^ ]+\.[a-z]{2,}$/;
      if (!emailPattern.test(email.value)) {
        e.preventDefault();
        alert('Please enter a valid email address.');
        return;
      }

      if (password.value.length < 6) {
        e.preventDefault();
        alert('Password must be at least 6 characters.');
      }
    });
  }

  // === REGISTER SCRIPT ===
  const registerForm = document.querySelector('#register-form');
  if (registerForm) {
    const name = registerForm.querySelector('input[name="name"]');
    const email = registerForm.querySelector('input[name="email"]');
    const password = registerForm.querySelector('input[name="password"]');
    const confirm = registerForm.querySelector('input[name="confirm_password"]');
    const toggleBtn = registerForm.querySelector('.toggle-password');
    const phoneInput = document.querySelector('input[name="phone_number"]');
    const ageInput = document.querySelector('input[name="age"]');

    toggleBtn?.addEventListener('click', () => {
      password.type = password.type === 'password' ? 'text' : 'password';
      toggleBtn.textContent = password.type === 'password' ? 'Show' : 'Hide';
    });

    registerForm.addEventListener('submit', (e) => {
      if (!name.value || !email.value || !password.value || !confirm.value || !phoneInput.value || !age.value) {
        e.preventDefault();
        alert('Please fill in all fields.');
        return;
      }

      const namePattern = /^[A-Za-z\s]+$/;
      if (!namePattern.test(name.value)) {
        e.preventDefault();
        alert('Name should contain only letters and spaces.');
        return;
      }

      const emailPattern = /^[^ ]+@[^ ]+\.[a-z]{2,}$/;
      if (!emailPattern.test(email.value)) {
        e.preventDefault();
        alert('Please enter a valid email address.');
        return;
      }

      const phonePattern = /^[0-9]{10}$/;
      if (!phonePattern.test(phoneInput.value)) {
        e.preventDefault();
        alert("Phone number must be exactly 10 digits.");
        return;
      }

      if (password.value.length < 6) {
        e.preventDefault();
        alert('Password must be at least 6 characters.');
        return;
      }

      if (password.value !== confirm.value) {
        e.preventDefault();
        alert('Passwords do not match.');
      }

      const age = parseInt(ageInput.value);
      if (isNaN(age) || age < 18) {
        e.preventDefault();
        alert("You must be 18 years or older to register.");
        return; 
      }
    });
  }

  // === INTERVIEW PRACTICE SCRIPT ===
  const roleSelect = document.getElementById("roleSelect");
  const container = document.getElementById("interviewContainer");
  const questionBox = document.getElementById("questionBox");
  const answerInput = document.getElementById("answerInput");
  const submitBtn = document.getElementById("submitAnswerBtn");
  const feedbackBox = document.getElementById("feedbackBox");
  const progressBox = document.getElementById("progressBox");

  let questions = [];
  let currentIndex = 0;
  let role = "";
  let correctCount = 0;

  roleSelect?.addEventListener("change", () => {
    role = roleSelect.value;
    if (!role) return;

    fetch("/interviewanswers", {
      method: "POST",
      headers: { "Content-Type": "application/x-www-form-urlencoded" },
      body: `role=${encodeURIComponent(role)}`
    })
      .then(res => res.json())
      .then(data => {
        questions = data.questions || [];
        currentIndex = 0;
        correctCount = 0;  
        if (questions.length > 0) {
          container.style.display = "block";
          showQuestion();
        } else {
          questionBox.textContent = "❌ No questions received.";
        }
      });
  });

  function showQuestion() {
    feedbackBox.textContent = "";
    answerInput.style.display = "block";
    submitBtn.disabled = false;
    answerInput.value = "";
    questionBox.textContent = questions[currentIndex];
    progressBox.textContent = `Question ${currentIndex + 1} of ${questions.length}`;
  }

  submitBtn?.addEventListener("click", () => {
    const answer = answerInput.value.trim();
    if (!answer) {
      alert("Please enter your answer.");
      return;
    }

    fetch("/save_interview_answer", {
      method: "POST",
      headers: { "Content-Type": "application/x-www-form-urlencoded" },
      body: `role=${encodeURIComponent(role)}&question=${encodeURIComponent(questions[currentIndex])}&answer=${encodeURIComponent(answer)}&current_question_index=${currentIndex}`
    })
      .then(() => {
        return fetch("/evaluate_answer", {
          method: "POST",
          headers: { "Content-Type": "application/x-www-form-urlencoded" },
          body: `question=${encodeURIComponent(questions[currentIndex])}&answer=${encodeURIComponent(answer)}`
        });
      })
      .then(res => res.json())
      .then(data => {
        const result = data.feedback?.toLowerCase();
        if (result === "correct") {
          feedbackBox.textContent = "✅ Correct";
          correctCount++;
        } else if (result === "wrong") {
          feedbackBox.textContent = "❌ Wrong";
        } else {
          feedbackBox.textContent = "⚠️ Could not evaluate answer.";
        }

        currentIndex++;
        if (currentIndex < questions.length) {
          setTimeout(() => showQuestion(), 1000);
        } else {
          setTimeout(() => {
            questionBox.textContent = `✅ You’ve completed all questions!\n🎯 Your score: ${correctCount} out of ${questions.length}`;
            answerInput.style.display = "none";
            submitBtn.disabled = true;
            progressBox.textContent = "";
          }, 1000);
        }
      });
  });

  // === RESUME SCRIPT ===
  const resumeForm = document.querySelector('#resume-form');
  if (resumeForm) {
    const fileInput = resumeForm.querySelector('input[name="resume"]');
    const textarea = resumeForm.querySelector('textarea[name="job_description"]');
    const feedbackBox = document.querySelector('.feedback-section p');

    resumeForm.addEventListener('submit', (e) => {
      const hasFile = fileInput.files.length > 0;
      const hasText = textarea.value.trim().length > 0;

      if (!hasFile || !hasText) {
        e.preventDefault();
        alert("Please upload your resume and fill in the job description.");
      } else {
        feedbackBox.textContent = "✅ Resume submitted! AI is analyzing it...";
      }
    });
  }

  // === COVER LETTER SCRIPT ===
  const coverForm = document.querySelector('#cover-form');
  if (coverForm) {
    const jobInput = coverForm.querySelector('textarea[name="job_description"]');
    const output = document.querySelector('#coverOutput');

    coverForm.addEventListener('submit', (e) => {
      const jobText = jobInput.value.trim();
      if (!jobText) {
        e.preventDefault();
        alert("Please enter a job title or job description.");
        return;
      }
      output.textContent = `✅ Generating a cover letter for: "${jobText}"...`;
    });
  }

  // === TRACKER SCRIPT ===
  const trackerForm = document.querySelector('#tracker-form');
  if (trackerForm) {
    const companyInput = trackerForm.querySelector('input[name="company"]');
    const titleInput = trackerForm.querySelector('input[name="title"]');
    const statusSelect = trackerForm.querySelector('select[name="status"]');
    const feedbackBox = document.querySelector('#trackerFeedback');

    trackerForm.addEventListener('submit', (e) => {
      const company = companyInput.value.trim();
      const title = titleInput.value.trim();
      const status = statusSelect.value;

      if (!company || !title || !status) {
        e.preventDefault();
        alert("Please fill out all fields.");
        return;
      }

      if (feedbackBox) {
        feedbackBox.textContent = `✅ Added "${title}" at ${company} with status "${status}"`;
        feedbackBox.style.color = 'green';
      }
    });
  }

  // === PROMPT PLAYGROUND SCRIPT ===
  const promptForm = document.querySelector('#prompt-form');
  if (promptForm) {
    const promptInput = promptForm.querySelector('textarea[name="prompt_text"]');
    const output = document.querySelector('#promptResponse');

    promptForm.addEventListener('submit', (e) => {
      const prompt = promptInput.value.trim();
      if (!prompt) {
        e.preventDefault();
        alert("Please enter a prompt.");
        return;
      }

      e.preventDefault();
      output.textContent = `🤖 AI is responding to: "${prompt}"\n\n[This is a simulated response. LLM API integration will replace this.]`;
    });
  }

});
