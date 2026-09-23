PY ?= python3
EXPERIMENTS := $(wildcard experiments/*)

.PHONY: all exp001 exp002 videos clean

all: exp001 exp002

exp001:
	cd experiments/001-collapse-as-rollback && for f in sims/*.py; do echo "▶ $$f"; $(PY) $$f || exit 1; done

exp002:
	cd experiments/002-gravity-as-compute-load && for f in sims/*.py; do echo "▶ $$f"; $(PY) $$f || exit 1; done

videos:
	for d in $(EXPERIMENTS); do [ -x $$d/video/build.sh ] && (cd $$d && ./video/build.sh); done; true

clean:
	rm -rf experiments/*/output/*.mp4 experiments/*/video/build/
