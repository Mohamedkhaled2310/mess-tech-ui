'use client';

import React, { useState } from 'react';
import Link from 'next/link';
import { useRouter } from 'next/navigation';
import { useLanguage } from '@/context/LanguageContext';
import { useCartStore } from '@/stores/useCartStore';
import { formatPrice } from '@/lib/utils';
import { ShieldCheck, Truck, Banknote, ArrowLeft, ArrowRight, CheckCircle2 } from 'lucide-react';

const GOVERNORATES = [
  { nameAr: 'القاهرة', nameEn: 'Cairo', fee: 50 },
  { nameAr: 'الجيزة', nameEn: 'Giza', fee: 50 },
  { nameAr: 'الإسكندرية', nameEn: 'Alexandria', fee: 60 },
  { nameAr: 'القليوبية', nameEn: 'Qalyubia', fee: 60 },
  { nameAr: 'الشرقية', nameEn: 'Sharqia', fee: 70 },
  { nameAr: 'الدقهلية (المنصورة)', nameEn: 'Dakahlia (Mansoura)', fee: 70 },
  { nameAr: 'الغربية (طنطا)', nameEn: 'Gharbia (Tanta)', fee: 70 },
  { nameAr: 'المنوفية', nameEn: 'Monufia', fee: 70 },
  { nameAr: 'البحيرة', nameEn: 'Beheira', fee: 70 },
  { nameAr: 'الإسماعيلية', nameEn: 'Ismailia', fee: 75 },
  { nameAr: 'السويس', nameEn: 'Suez', fee: 75 },
  { nameAr: 'بورسعيد', nameEn: 'Port Said', fee: 75 },
  { nameAr: 'أسيوط', nameEn: 'Asyut', fee: 90 },
  { nameAr: 'سوهاج', nameEn: 'Sohag', fee: 95 },
  { nameAr: 'قنا والأقصر وأسوان', nameEn: 'Qena, Luxor & Aswan', fee: 100 },
];

export default function CheckoutPage() {
  const router = useRouter();
  const { locale, dir, t } = useLanguage();
  const { items, getSubtotal, clearCart } = useCartStore();

  const [fullName, setFullName] = useState('');
  const [phone, setPhone] = useState('');
  const [governorate, setGovernorate] = useState(GOVERNORATES[0].nameAr);
  const [city, setCity] = useState('');
  const [address, setAddress] = useState('');
  const [notes, setNotes] = useState('');
  const [isSubmitting, setIsSubmitting] = useState(false);

  const subtotal = getSubtotal();
  const selectedGovObj = GOVERNORATES.find((g) => g.nameAr === governorate) || GOVERNORATES[0];
  const shippingFee = subtotal >= 10000 ? 0 : selectedGovObj.fee;
  const total = subtotal + shippingFee;

  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault();
    if (!fullName || !phone || !address) {
      alert('يرجى ملء جميع البيانات الأساسية (الاسم، الهاتف، العنوان)');
      return;
    }

    setIsSubmitting(true);
    const orderNumber = `MESS-${Math.floor(100000 + Math.random() * 900000)}`;

    setTimeout(() => {
      clearCart();
      router.push(`/track-order?order=${orderNumber}&phone=${phone}`);
    }, 1000);
  };

  if (items.length === 0) {
    return (
      <div className="max-w-xl mx-auto py-16 px-4 text-center space-y-4">
        <h2 className="text-xl font-bold text-slate-800">{t('cartEmpty')}</h2>
        <p className="text-xs text-slate-500">{t('cartEmptyDesc')}</p>
        <Link
          href="/"
          className="inline-block px-5 py-2.5 rounded-xl bg-petrol-700 text-white font-bold text-xs"
        >
          {t('startShopping')}
        </Link>
      </div>
    );
  }

  return (
    <div className="max-w-6xl mx-auto px-4 sm:px-6 lg:px-8 py-10">
      <div className="mb-8 text-center sm:text-start">
        <h1 className="text-2xl sm:text-3xl font-black text-petrol-900">{t('checkoutTitle')}</h1>
        <p className="text-xs sm:text-sm text-slate-500">{t('checkoutSubtitle')}</p>
      </div>

      <div className="grid grid-cols-1 lg:grid-cols-3 gap-8">
        {/* Form */}
        <div className="lg:col-span-2">
          <form onSubmit={handleSubmit} className="bg-white p-6 rounded-2xl border border-slate-200 shadow-subtle space-y-6">
            <h3 className="font-extrabold text-base text-petrol-900 border-b border-slate-100 pb-3">
              1. بيانات الشحن والتوصيل
            </h3>

            <div className="grid grid-cols-1 sm:grid-cols-2 gap-4">
              <div>
                <label className="block text-xs font-bold text-slate-700 mb-1">{t('fullName')} *</label>
                <input
                  type="text"
                  required
                  value={fullName}
                  onChange={(e) => setFullName(e.target.value)}
                  placeholder="مثال: محمد خالد أحمد"
                  className="w-full px-3.5 py-2.5 text-xs rounded-xl border border-slate-200 focus:outline-none focus:ring-2 focus:ring-petrol-500"
                />
              </div>

              <div>
                <label className="block text-xs font-bold text-slate-700 mb-1">{t('phoneNumber')} *</label>
                <input
                  type="tel"
                  required
                  value={phone}
                  onChange={(e) => setPhone(e.target.value)}
                  placeholder="010XXXXXXXX"
                  className="w-full px-3.5 py-2.5 text-xs rounded-xl border border-slate-200 focus:outline-none focus:ring-2 focus:ring-petrol-500 font-mono"
                />
              </div>

              <div>
                <label className="block text-xs font-bold text-slate-700 mb-1">{t('governorate')} *</label>
                <select
                  value={governorate}
                  onChange={(e) => setGovernorate(e.target.value)}
                  className="w-full px-3.5 py-2.5 text-xs rounded-xl border border-slate-200 focus:outline-none focus:ring-2 focus:ring-petrol-500 font-bold"
                >
                  {GOVERNORATES.map((g) => (
                    <option key={g.nameAr} value={g.nameAr}>
                      {locale === 'ar' ? g.nameAr : g.nameEn} ({g.fee} ج.م)
                    </option>
                  ))}
                </select>
              </div>

              <div>
                <label className="block text-xs font-bold text-slate-700 mb-1">{t('cityArea')} *</label>
                <input
                  type="text"
                  required
                  value={city}
                  onChange={(e) => setCity(e.target.value)}
                  placeholder="مثال: التجمع الخامس / مدينة نصر"
                  className="w-full px-3.5 py-2.5 text-xs rounded-xl border border-slate-200 focus:outline-none focus:ring-2 focus:ring-petrol-500"
                />
              </div>
            </div>

            <div>
              <label className="block text-xs font-bold text-slate-700 mb-1">{t('detailedAddress')} *</label>
              <textarea
                rows={2}
                required
                value={address}
                onChange={(e) => setAddress(e.target.value)}
                placeholder="اسم الشارع، رقم العمارة، رقم الشقة أو اسم الشركة"
                className="w-full px-3.5 py-2.5 text-xs rounded-xl border border-slate-200 focus:outline-none focus:ring-2 focus:ring-petrol-500"
              />
            </div>

            <div>
              <label className="block text-xs font-bold text-slate-700 mb-1">{t('orderNotes')}</label>
              <input
                type="text"
                value={notes}
                onChange={(e) => setNotes(e.target.value)}
                placeholder="ملاحظات تسليم خاصة أو أوقات مفضلة للاتصال"
                className="w-full px-3.5 py-2.5 text-xs rounded-xl border border-slate-200 focus:outline-none focus:ring-2 focus:ring-petrol-500"
              />
            </div>

            {/* Payment selection */}
            <div className="pt-4 border-t border-slate-100 space-y-3">
              <h3 className="font-extrabold text-base text-petrol-900">2. {t('paymentMethodTitle')}</h3>

              <div className="p-4 rounded-xl border-2 border-petrol-700 bg-petrol-50/50 flex items-start gap-3">
                <div className="w-5 h-5 rounded-full border-2 border-petrol-700 flex items-center justify-center shrink-0 mt-0.5">
                  <div className="w-2.5 h-2.5 rounded-full bg-petrol-700" />
                </div>
                <div>
                  <h4 className="font-extrabold text-xs text-petrol-900 flex items-center gap-2">
                    <Banknote className="w-4 h-4 text-emerald-600" />
                    <span>{t('codLabel')}</span>
                  </h4>
                  <p className="text-xs text-slate-500 mt-1">{t('codDesc')}</p>
                </div>
              </div>
            </div>

            <button
              type="submit"
              disabled={isSubmitting}
              className="w-full py-4 rounded-xl bg-petrol-700 hover:bg-petrol-800 disabled:bg-slate-400 text-white font-black text-sm flex items-center justify-center gap-2 shadow-lg hover:shadow-xl transition-all"
            >
              <span>{isSubmitting ? 'جاري تسجيل الطلب...' : t('confirmOrderBtn')}</span>
              {dir === 'rtl' ? <ArrowLeft className="w-4 h-4" /> : <ArrowRight className="w-4 h-4" />}
            </button>
          </form>
        </div>

        {/* Order Summary */}
        <div>
          <div className="bg-white p-5 rounded-2xl border border-slate-200 shadow-subtle space-y-4 sticky top-24">
            <h3 className="font-extrabold text-sm text-petrol-900 border-b border-slate-100 pb-3">
              {t('orderSummary')} ({items.length} {t('items')})
            </h3>

            <div className="max-h-60 overflow-y-auto space-y-3 divide-y divide-slate-100">
              {items.map((it) => (
                <div key={it.product.id} className="pt-2 first:pt-0 flex items-center gap-3">
                  <img src={it.product.image} alt={it.product.name[locale]} className="w-12 h-12 object-contain shrink-0" />
                  <div className="flex-1 min-w-0">
                    <h5 className="font-bold text-xs text-petrol-950 line-clamp-1">{it.product.name[locale]}</h5>
                    <span className="text-[10px] text-slate-400 font-mono">الكمية: {it.quantity}</span>
                  </div>
                  <span className="font-mono font-bold text-xs text-petrol-900">
                    {formatPrice(it.product.price * it.quantity, locale)}
                  </span>
                </div>
              ))}
            </div>

            <div className="border-t border-slate-100 pt-3 space-y-2 text-xs">
              <div className="flex justify-between text-slate-600">
                <span>{t('subtotal')}</span>
                <span className="font-mono font-bold">{formatPrice(subtotal, locale)}</span>
              </div>
              <div className="flex justify-between text-slate-600">
                <span>{t('shipping')} ({selectedGovObj.nameAr})</span>
                <span className="font-mono font-bold text-emerald-600">
                  {shippingFee === 0 ? t('freeShipping') : formatPrice(shippingFee, locale)}
                </span>
              </div>
              <div className="flex justify-between text-sm font-black text-petrol-900 border-t border-slate-200 pt-2">
                <span>{t('total')}</span>
                <span className="font-mono text-base text-petrol-900">{formatPrice(total, locale)}</span>
              </div>
            </div>

            <div className="p-3 rounded-xl bg-emerald-50 border border-emerald-100 flex items-center gap-2 text-emerald-800 text-xs">
              <CheckCircle2 className="w-4 h-4 shrink-0 text-emerald-600" />
              <span>معاينة المنتجات متاحة عند الاستلام قبل السداد</span>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
}
