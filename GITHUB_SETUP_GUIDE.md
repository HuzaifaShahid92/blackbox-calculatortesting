# GitHub Repository Setup Guide

## Steps to Create GitHub Repository

### 1. Create GitHub Account (if you don't have one)
- Visit: https://github.com/signup
- Complete the registration

### 2. Create a New Repository
- Go to: https://github.com/new
- Repository name: `blackbox-calculator-testing`
- Description: "Blackbox Testing Assignment - Calculator Application with 52 Test Cases"
- Choose: Public (for submission purposes)
- Initialize with README: No (we have our own)
- Click "Create repository"

### 3. Initialize Local Repository
```bash
cd c:\Users\Huzaifa\OneDrive\Desktop\CODE\blackbox_testing_assignment
git init
```

### 4. Configure Git (First time only)
```bash
git config --global user.name "Your Name"
git config --global user.email "your.email@example.com"
```

### 5. Add Remote Repository
```bash
git remote add origin https://github.com/YOUR_USERNAME/blackbox-calculator-testing.git
```

### 6. Stage All Files
```bash
git add .
```

### 7. Create Initial Commit
```bash
git commit -m "Initial commit: Blackbox testing assignment with 52 test cases"
```

### 8. Push to GitHub
```bash
git branch -M main
git push -u origin main
```

### 9. Verify on GitHub
- Visit: https://github.com/YOUR_USERNAME/blackbox-calculator-testing
- Verify all files are uploaded:
  - calculator.py
  - test_calculator.py
  - BLACKBOX_TESTING_REPORT.md
  - README.md
  - .gitignore

---

## Complete Command Sequence

```bash
# Navigate to project directory
cd "c:\Users\Huzaifa\OneDrive\Desktop\CODE\blackbox_testing_assignment"

# Initialize git repository
git init

# Configure git (one-time setup)
git config --global user.name "Huzaifa"
git config --global user.email "your.email@example.com"

# Add remote repository (replace USERNAME with your GitHub username)
git remote add origin https://github.com/USERNAME/blackbox-calculator-testing.git

# Stage all files
git add .

# Create commit
git commit -m "Initial commit: Blackbox testing assignment - Calculator application with 52 comprehensive test cases"

# Rename branch to main (if needed)
git branch -M main

# Push to GitHub
git push -u origin main
```

---

## After Setup

### To Push Future Changes:
```bash
git add .
git commit -m "Your commit message"
git push origin main
```

### To Check Status:
```bash
git status
```

### To View Commit History:
```bash
git log
```

---

## Files to Include in Repository

```
📦 blackbox-calculator-testing/
 ├── 📄 calculator.py                    (Main application code)
 ├── 📄 test_calculator.py              (52 test cases)
 ├── 📄 BLACKBOX_TESTING_REPORT.md      (Detailed report)
 ├── 📄 README.md                       (Documentation)
 └── 📄 .gitignore                      (Git configuration)
```

---

## Submission Checklist

- [ ] GitHub account created
- [ ] Repository created on GitHub
- [ ] Local repository initialized
- [ ] All files committed
- [ ] Files pushed to GitHub
- [ ] Verify repository is public and accessible
- [ ] Copy repository URL for submission: `https://github.com/YOUR_USERNAME/blackbox-calculator-testing`

---

## Repository URL for Submission

After completing all steps, your submission will be:

**GitHub Repository URL:** `https://github.com/YOUR_USERNAME/blackbox-calculator-testing`

---

## Need Help?

### Common Issues:

1. **"Permission denied" when pushing**
   - Solution: Use HTTPS URL or set up SSH keys
   - Reference: https://docs.github.com/en/authentication/connecting-to-github-with-ssh

2. **"Repository already exists"**
   - Remove .git folder: `rm -r .git` (Windows: `rmdir .git /s`)
   - Re-initialize: `git init`

3. **"Fatal: not a git repository"**
   - Make sure you're in the correct directory
   - Run: `git init`

4. **Files not appearing on GitHub**
   - Verify: `git status`
   - Ensure files are committed and pushed
   - Check: `git log`

---

## GitHub Links for Assignment

Once uploaded, provide these links to your instructor:

1. **Repository URL:** https://github.com/YOUR_USERNAME/blackbox-calculator-testing
2. **Test File:** https://github.com/YOUR_USERNAME/blackbox-calculator-testing/blob/main/test_calculator.py
3. **Report:** https://github.com/YOUR_USERNAME/blackbox-calculator-testing/blob/main/BLACKBOX_TESTING_REPORT.md
4. **Project Code:** https://github.com/YOUR_USERNAME/blackbox-calculator-testing/blob/main/calculator.py

---

## Assignment Submission

### Expected Deliverables ✓
1. **Project Code** ✓ - calculator.py (in GitHub)
2. **Detailed Report** ✓ - BLACKBOX_TESTING_REPORT.md (in GitHub)
3. **GitHub Link** ✓ - https://github.com/YOUR_USERNAME/blackbox-calculator-testing

### All requirements are ready for submission!
