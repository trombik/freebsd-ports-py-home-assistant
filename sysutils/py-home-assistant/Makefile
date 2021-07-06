# $FreeBSD$

PORTNAME=	home-assistant
DISTVERSION=	2021.6.6
CATEGORIES=	sysutils python
MASTER_SITES=	CHEESESHOP
PKGNAMEPREFIX=	${PYTHON_PKGNAMEPREFIX}

MAINTAINER=	y@trombik.org
COMMENT=	Open source home automation that puts local control and privacy first

LICENSE=	APACHE20
LICENSE_FILE=	${WRKSRC}/LICENSE.md

RUN_DEPENDS=	${PYTHON_PKGNAMEPREFIX}aiohttp>0:www/py-aiohttp@${PY_FLAVOR} \
	${PYTHON_PKGNAMEPREFIX}astral>0:devel/py-astral@${PY_FLAVOR} \
	${PYTHON_PKGNAMEPREFIX}async_timeout>0:devel/py-async_timeout@${PY_FLAVOR} \
	${PYTHON_PKGNAMEPREFIX}attrs>0:devel/py-attrs@${PY_FLAVOR} \
	${PYTHON_PKGNAMEPREFIX}bcrypt>0:security/py-bcrypt@${PY_FLAVOR} \
	${PYTHON_PKGNAMEPREFIX}certifi>0:security/py-certifi@${PY_FLAVOR} \
	${PYTHON_PKGNAMEPREFIX}ciso8601>0:textproc/py-ciso8601@${PY_FLAVOR} \
	${PYTHON_PKGNAMEPREFIX}cryptography>0:security/py-cryptography@${PY_FLAVOR} \
	${PYTHON_PKGNAMEPREFIX}importlib-metadata>0:devel/py-importlib-metadata@${PY_FLAVOR} \
	${PYTHON_PKGNAMEPREFIX}Jinja2>0:devel/py-Jinja2@${PY_FLAVOR} \
	${PYTHON_PKGNAMEPREFIX}pyjwt>0:www/py-pyjwt@${PY_FLAVOR} \
	${PYTHON_PKGNAMEPREFIX}pip>0:devel/py-pip@${PY_FLAVOR} \
	${PYTHON_PKGNAMEPREFIX}pytz>0:devel/py-pytz@${PY_FLAVOR} \
	${PYTHON_PKGNAMEPREFIX}requests>0:www/py-requests@${PY_FLAVOR} \
	${PYTHON_PKGNAMEPREFIX}ruamel.yaml>0:devel/py-ruamel.yaml@${PY_FLAVOR} \
	${PYTHON_PKGNAMEPREFIX}ruamel.yaml.clib>0:devel/py-ruamel.yaml.clib@${PY_FLAVOR} \
	${PYTHON_PKGNAMEPREFIX}python-slugify>0:textproc/py-python-slugify@${PY_FLAVOR} \
	${PYTHON_PKGNAMEPREFIX}voluptuous>0:devel/py-voluptuous@${PY_FLAVOR} \
	${PYTHON_PKGNAMEPREFIX}voluptuous-serialize>0:devel/py-voluptuous-serialize@${PY_FLAVOR} \
	${PYTHON_PKGNAMEPREFIX}aiohttp_cors>0:www/py-aiohttp_cors@${PY_FLAVOR} \
	${PYTHON_PKGNAMEPREFIX}sqlalchemy13>0:databases/py-sqlalchemy13@${PY_FLAVOR} \
	${PYTHON_PKGNAMEPREFIX}yarl>0:www/py-yarl@${PY_FLAVOR} \
	${PYTHON_PKGNAMEPREFIX}yaml>0:devel/py-yaml@${PY_FLAVOR} \
	${PYTHON_PKGNAMEPREFIX}awesomeversion>0:devel/py-awesomeversion@${PY_FLAVOR} \
	${PYTHON_PKGNAMEPREFIX}backports.zoneinfo>0:devel/py-backports.zoneinfo@${PY_FLAVOR} \
	${PYTHON_PKGNAMEPREFIX}httpx>0:www/py-httpx@${PY_FLAVOR} \
	${PYTHON_PKGNAMEPREFIX}markupsafe>0:textproc/py-markupsafe@${PY_FLAVOR} \
	${PYTHON_PKGNAMEPREFIX}pillow>0:graphics/py-pillow@${PY_FLAVOR} \
	${PYTHON_PKGNAMEPREFIX}aiodiscover>0:net/py-aiodiscover@${PY_FLAVOR} \
	${PYTHON_PKGNAMEPREFIX}mutagen>0:audio/py-mutagen@${PY_FLAVOR} \
	${PYTHON_PKGNAMEPREFIX}cryptography>0:security/py-cryptography@${PY_FLAVOR}

USES=		python:3.7+
USE_PYTHON=	autoplist distutils

USE_GITHUB=	yes
GH_TUPLE=	home-assistant:core:${DISTVERSION}
NO_ARCH=	yes

pre-configure:
	${REINPLACE_CMD} 's/==/>=/g' \
		${WRKSRC}/setup.py ${WRKSRC}/requirements.txt ${WRKSRC}/homeassistant/package_constraints.txt
	${RM} ${WRKSRC}/*.orig ${WRKSRC}/*.bak ${WRKSRC}/homeassistant/*.orig ${WRKSRC}/homeassistant/*.bak

.include <bsd.port.mk>
