const expand = (e) => {
    let parent = e.target.parentElement;
    let child = parent.children[1];
    let svg;
    if (e.srcElement) {
      svg = e.srcElement.children[0];
    } else {
      svg = e.originalTarget.children[0];
    }
    if (child.classList.contains("collapse")) {
      child.classList.remove("collapse");
      svg.classList.remove("upsideDown");
    } else {
      child.classList.add("collapse");
      svg.classList.add("upsideDown");
    }
  };
  