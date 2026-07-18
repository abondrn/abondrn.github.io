JEKYLL=jekyll-digital-garden

serve: build
	cd $(JEKYLL) && bundle exec jekyll serve --trace

bundle:
	cd $(JEKYLL) && sudo gem install bundle

lock:
	cd $(JEKYLL) && bundle lock --add-platform x86_64-linux

build:
	cd $(JEKYLL) && bundle install