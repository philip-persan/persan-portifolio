module.exports = {
  content: [
    "./frontend/**/*.{html,js}",
    "./frontend/index.html",
    "./frontend/about.html",
    "./frontend/skills.html",
    "./frontend/contact.html",
    "./frontend/work.html",
    "./about/templates/about/pages/about.html",
    "./about/templates/contact/pages/contact.html",
    "./about/templates/skills/pages/skills.html",
    "./about/templates/work/pages/portifolio.html",
  ],
  theme: {
    extend: {
      colors: {
        primary: "#222831",
        secondary: "#393E46",
        orangeC: "#D65A31",
        EEE: "#EEEEEE",
      },
    },
  },
  plugins: [
    require("@tailwindcss/typography"),
    require("@tailwindcss/forms"),
    require("@tailwindcss/line-clamp"),
    require("@tailwindcss/aspect-ratio"),
  ],
};
