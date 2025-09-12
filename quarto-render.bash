export TARGET="_site"
export TARGET_FROM_SUBDIR="../${TARGET}/"
export SUBDIR="sunumlar"
export SLIDES="sunum-LLM-giris-2025"

mkdir -p $TARGET
cd $SUBDIR
quarto render "${SLIDES}.qmd" --to html
cd ..
quarto render --to html
ls $TARGET
cp "$SUBDIR/${SLIDES}.html" $TARGET
cp -r "$SUBDIR/${SLIDES}_files" $TARGET
ls $TARGET
