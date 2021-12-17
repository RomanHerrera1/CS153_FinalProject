The model is the Google Inception v3., with its 
last layer retrained on a new dataset. It has 3
labels: artificial cat, real cat, and neither.
Artificial cats are trained on the attached artificial
cat dataset that was handmade for this model. The 
real cat and neither categories used the image dataset
from https://www.kaggle.com/alessiocorrado99/animals10.
This means, neither includes: dog, horse, elephant, butterfly,
squirel, chicken, cow, sheep, and spider.

If you want to run the code, you will need to download the kaggle dataset
and create folders for real cats and the neither category again.
(could not upload because too many images) You can try to use the move_files.py
to make that quicker but there may be some pathing errors to watch for.

I followed the guides from 

For the youTube frame-collection, I used https://stackoverflow.com/questions/50876292/capture-youtube-video-for-further-processing-without-downloading-the-video but it did not work for me because of YouTube changes currrently but maybe it will work for you.
