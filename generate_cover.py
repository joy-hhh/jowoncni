from jinja2 import Template
from pathlib import Path
import subprocess

# 현재 파일 경로 기준 디렉토리
BASE_DIR = Path(__file__).resolve().parent
TEMPLATE_PATH = BASE_DIR / "cover_template.tex"
LOGO_FILE = BASE_DIR / "logo.png"  # 로고 파일이 있으면 이 경로로 두세요

def generate_pdf(company, target, date, output_name="cover"):
    # 템플릿 읽기
    template_text = TEMPLATE_PATH.read_text(encoding="utf-8")
    template = Template(template_text)
    rendered = template.render(회사명=company, 평가대상명=target, 날짜=date)

    # TeX 파일 저장
    tex_path = BASE_DIR / f"{output_name}.tex"
    tex_path.write_text(rendered, encoding="utf-8")

    # LaTeX 컴파일
    subprocess.run(["xelatex", tex_path.name], cwd=BASE_DIR, check=True)

    # cleanup (선택)
    tex_path.unlink(missing_ok=True)

# 테스트 실행 예시 (단독 실행 시)
if __name__ == "__main__":
    generate_pdf("주식회사 조원씨앤아이", "사단법인 한국알사용자회", "2025년 1월 10일")
