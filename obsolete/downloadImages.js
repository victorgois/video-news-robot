const download = require('image-downloader');

const options = {
    url : 'https://s2.glbimg.com/sgFYvzTM-UPasf_ZsgtXnK_01s8=/1200x/smart/filters:cover():strip_icc()/i.s3.glbimg.com/v1/AUTH_63b422c2caee4269b8b34177e8876b93/internal_photos/bs/2019/w/n/3Nr1nmT2Se8jEWKGf8zQ/ap-16176694409826.jpg',
    dest : './images/'
}

async function downloadIMG() {
    try {
      const { filename, image } = await download.image(options)
      console.log(filename) // => /path/to/dest/image.jpg
    } catch (e) {
      console.error(e)
    }
  }
   
  downloadIMG()