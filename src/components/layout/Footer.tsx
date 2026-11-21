'use client';

import React from 'react';
import Link from 'next/link';
import { useLanguage } from '@/context/LanguageContext';
import { Phone, Mail, MapPin, ShieldCheck, Heart } from 'lucide-react';

export default function Footer() {
  const { t } = useLanguage();

  return (
    <footer className="bg-petrol-950 text-white pt-12 pb-6 border-t border-petrol-900">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-8 pb-10 border-b border-petrol-800/80">
          {/* Brand Info */}
          <div className="space-y-4">
            <div className="flex items-center gap-2.5">
              <div className="w-9 h-9 rounded-xl bg-petrol-700 flex items-center justify-center text-white font-black text-lg border border-petrol-600">
                M
              </div>
              <span className="font-extrabold text-xl tracking-tight text-white">
                MESS <span className="text-sky-400">TECH</span>
              </span>
            </div>
            <p className="text-xs text-slate-300 leading-relaxed">{t('footerAbout')}</p>
            <div className="flex items-center gap-2 text-xs text-sky-300">
              <ShieldCheck className="w-4 h-4 text-emerald-400" />
              <span>{t('officialAgent')}</span>
            </div>
          </div>

          {/* Quick Links */}
          <div>
            <h4 className="font-bold text-sm text-white mb-3.5 border-b border-petrol-800 pb-2">
              {t('quickLinks')}
            </h4>
            <ul className="space-y-2 text-xs text-slate-300">
              <li>
                <Link href="/" className="hover:text-sky-400 transition-colors">
                  {t('nav_home')}
                </Link>
              </li>
              <li>
                <Link href="/catalog" className="hover:text-sky-400 transition-colors">
                  {t('featuredProductsTitle')}
                </Link>
              </li>
              <li>
                <Link href="/track-order" className="hover:text-sky-400 transition-colors">
                  {t('trackOrder')}
                </Link>
              </li>
              <li>
                <Link href="/compare" className="hover:text-sky-400 transition-colors">
                  {t('compare')}
                </Link>
              </li>
              <li>
                <Link href="/admin/orders" className="hover:text-amber-300 text-amber-400 transition-colors">
                  ⚙️ {t('adminDashboard')}
                </Link>
              </li>
            </ul>
          </div>

          {/* Categories */}
          <div>
            <h4 className="font-bold text-sm text-white mb-3.5 border-b border-petrol-800 pb-2">
              {t('categories')}
            </h4>
            <ul className="space-y-2 text-xs text-slate-300">
              <li>
                <Link href="/catalog?category=switches" className="hover:text-sky-400 transition-colors">
                  {t('nav_switches')}
                </Link>
              </li>
              <li>
                <Link href="/catalog?category=wifi" className="hover:text-sky-400 transition-colors">
                  {t('nav_wifi')}
                </Link>
              </li>
              <li>
                <Link href="/catalog?category=storage" className="hover:text-sky-400 transition-colors">
                  {t('nav_storage')}
                </Link>
              </li>
              <li>
                <Link href="/catalog?category=ups" className="hover:text-sky-400 transition-colors">
                  {t('nav_ups')}
                </Link>
              </li>
              <li>
                <Link href="/catalog?category=passive" className="hover:text-sky-400 transition-colors">
                  {t('nav_passive')}
                </Link>
              </li>
            </ul>
          </div>

          {/* Contact Details */}
          <div>
            <h4 className="font-bold text-sm text-white mb-3.5 border-b border-petrol-800 pb-2">
              {t('contactUs')}
            </h4>
            <ul className="space-y-3 text-xs text-slate-300">
              <li className="flex items-center gap-2.5">
                <MapPin className="w-4 h-4 text-sky-400 shrink-0" />
                <span>{t('addressCairo')}</span>
              </li>
              <li className="flex items-center gap-2.5 font-mono">
                <Phone className="w-4 h-4 text-sky-400 shrink-0" />
                <span>+20 100 000 0000</span>
              </li>
              <li className="flex items-center gap-2.5 font-mono">
                <Mail className="w-4 h-4 text-sky-400 shrink-0" />
                <span>sales@mess-tech.store</span>
              </li>
            </ul>

            {/* Payment & Trust Badges */}
            <div className="mt-4 pt-3 border-t border-petrol-800">
              <span className="text-[11px] text-slate-400 block mb-1.5">{t('paymentMethodTitle')}:</span>
              <div className="flex items-center gap-2 flex-wrap text-[10px] font-bold">
                <span className="px-2 py-1 bg-petrol-800 text-sky-300 rounded border border-petrol-700">
                  💵 الدفع عند الاستلام COD
                </span>
                <span className="px-2 py-1 bg-petrol-800 text-emerald-300 rounded border border-petrol-700">
                  ⚡ InstaPay
                </span>
                <span className="px-2 py-1 bg-petrol-800 text-rose-300 rounded border border-petrol-700">
                  📱 Vodafone Cash
                </span>
              </div>
            </div>
          </div>
        </div>

        {/* Bottom copyright */}
        <div className="pt-6 flex flex-col sm:flex-row items-center justify-between text-xs text-slate-400 gap-3">
          <p>{t('allRightsReserved')}</p>
          <p className="flex items-center gap-1">
            <span>{t('poweredBy')}</span>
          </p>
        </div>
      </div>
    </footer>
  );
}
