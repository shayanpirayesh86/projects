
---

## interactive-portfolio-website/PortfolioWebsite.jsx

```jsx
import React from "react";
import { motion } from "framer-motion";

const sections = [
  { title: "Welcome", content: "Hi, I'm Shayan, a passionate developer." },
  { title: "About Me", content: "I love coding and creating innovative projects." },
  { title: "Projects", content: "Check out my work on GitHub." },
  { title: "Contact", content: "Get in touch via email or LinkedIn." },
];

export default function PortfolioWebsite() {
  return (
    <div style={{ fontFamily: "Arial, sans-serif", padding: 40 }}>
      {sections.map(({ title, content }, i) => (
        <motion.section
          key={i}
          initial={{ opacity: 0, y: 50 }}
          whileInView={{ opacity: 1, y: 0 }}
          viewport={{ once: true }}
          transition={{ duration: 0.6, delay: i * 0.3 }}
          style={{ marginBottom: 80 }}
        >
          <h2>{title}</h2>
          <p>{content}</p>
        </motion.section>
      ))}
    </div>
  );
}
