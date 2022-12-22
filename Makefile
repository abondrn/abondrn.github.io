JEKYLL=jekyll-digital-garden

serve: build
	cd $(JEKYLL) && bundle exec jekyll serve --trace

bundle:
	cd $(JEKYLL) && sudo gem install bundle

build:
	cd $(JEKYLL) && bundle install