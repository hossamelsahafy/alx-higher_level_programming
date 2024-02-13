#!/usr/bin/node
// Define Rectangle Class
class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0 && typeof w === 'number' && typeof h === 'number') {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    if (this.width && this.height) {
      for (let i = 0; i < this.height; i++) {
        let r = '';
        for (let j = 0; j < this.width; j++) {
          r += 'X';
        }
        console.log(r);
      }
    }
  }

  rotate () {
    if (this.width && this.height) {
      const tmp = this.width;
      this.width = this.height;
      this.height = tmp;
    }
  }

  double () {
    if (this.width && this.height) {
      this.width = this.width * 2;
      this.height = this.height * 2;
    }
  }
}
module.exports = Rectangle;
